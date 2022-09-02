# coding: utf-8
from __future__ import absolute_import

from contextlib import closing
from functools import reduce
from operator import and_
from os import path
import os

from django.apps import apps
from django.conf import settings
from django.db import connection
from django.db import connections
from django.db.models import Q
from django.db.models.fields import related
from django.db.transaction import atomic
from django.http import HttpRequest
from m3_django_compat import get_related
import six

from educommon import ioc
from educommon.audit_log.constants import EXCLUDED_TABLES
from educommon.audit_log.constants import PG_LOCK_ID
from educommon.audit_log.constants import SQL_FILES_DIR
from educommon.utils.misc import cached_property


def configure():
    u"""Изменяет параметры подключения к сервисной БД, обновляет триггеры."""
    params = get_db_connection_params()
    params['lock_id'] = PG_LOCK_ID
    execute_sql_file(
        'default',
        os.path.join(SQL_FILES_DIR, 'configure_audit_log.sql'),
        params
    )
    if getattr(settings, 'SELECTIVE_TABLES_LOG_ON', False):
        _set_audit_log_tables()
        execute_sql_file(
            'default',
            os.path.join(SQL_FILES_DIR, 'configure_selective_audit_log.sql'),
            params
        )


def _set_audit_log_tables():
    """Собирает логируемые таблицы."""
    from django.apps import apps

    table_names = set(
        model._meta.db_table
        for model in apps.get_models()
        if getattr(model, 'need_to_log', False)
    )

    Table = apps.get_model('audit_log', 'Table')
    AuditLog = apps.get_model('audit_log', 'AuditLog')

    # Создаются таблицы, на которые нужно навесить триггеры
    exists_table_names = set(
        Table.objects.filter(
            schema='public',
        ).values_list('name', flat=True)
    )

    table_names_for_creating = table_names.difference(exists_table_names)
    table_names_for_deleting = exists_table_names.difference(table_names)

    Table.objects.bulk_create(
        objs=[
            Table(name=table, schema='public')
            for table in table_names_for_creating
        ],
    )

    # В Django 1.11 не устанавливается ON DELETE CASCADE, поэтому подчистим логи заранее
    AuditLog.objects.filter(table__name__in=table_names_for_deleting).delete()

    # Удаление таблиц, изменение записей которых не должны логироваться
    Table.objects.filter(
        name__in=table_names_for_deleting,
    ).delete()


def is_initialized(database_alias):
    u"""Проверяет, проинициализированы ли средства журналирования.

    :param str database_alias: Алиас БД, в которой будет проверяться наличие
        средств журналирования.

    :rtype: bool
    """
    # Проверка наличия схемы audit.
    with closing(connections[database_alias].cursor()) as cursor:
        cursor.execute("select 1 from pg_namespace where nspname = 'audit'")
        if cursor.fetchone() is None:
            return False

    # Проверка наличия таблицы postgresql_errors
    with closing(connections[database_alias].cursor()) as cursor:
        cursor.execute(
            'select 1 '
            'from information_schema.tables '
            'where table_schema = %s and table_name = %s',
            ('audit', 'postgresql_errors')
        )
        if cursor.fetchone() is None:
            return False

    # Проверка наличия всех функций схемы.
    function_names = set((
        'get_param',
        'get_table_id',
        'on_modify',
        'update_triggers',
        'is_valid_options',
        'str_to_ip',
        'log_postgres_error',
        'set_for_selective_tables_triggers',
    ))
    for function_name in function_names:
        with closing(connections[database_alias].cursor()) as cursor:
            cursor.execute(
                "select 1 "
                "from pg_proc proc "
                "inner join pg_namespace ns on ns.oid = proc.pronamespace "
                "where proc.proname = %s and ns.nspname = %s "
                "limit 1",
                [function_name, 'audit']
            )
            if cursor.fetchone() is None:
                return False

    return True


def check_connection_fdw():
    u"""Проверяет подключение к сервисной БД через PostgreSQL FDW.

    :returns: Кортеж из двух элементов: первый указывает на работоспособность
        подключения (``True`` - есть, ``False`` - нет подключения), второй --
        содержит текст ошибки, если подключения нет.
    :rtype: tuple
    """
    with closing(connection.cursor()) as cursor:
        try:
            cursor.execute('SELECT 1 FROM "audit"."audit_log" LIMIT 1')
        except Exception as error:
            return False, str(error)
        else:
            return True, None


@atomic
def execute_sql_file(database_alias, file_name, params=None):
    u"""Исполняет SQL-скрипт, из файла по указанному пути."""
    cursor = connections[database_alias].cursor()

    file_path = path.join(path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        file_contents = f.read()

    if params:
        file_contents = file_contents.format(**params)

    cursor.execute(file_contents)


def get_db_connection_params():
    u"""Возвращает параметры подключения к сервисной БД."""
    target_db_conf = settings.DATABASES[settings.SERVICE_DB_ALIAS]
    return dict(
        host=target_db_conf['HOST'],
        dbname=target_db_conf['NAME'],
        port=target_db_conf['PORT'],
        user=target_db_conf['USER'],
        password=target_db_conf['PASSWORD']
    )


@atomic()
def set_db_param(key, value):
    u"""Устанавливает параметры в custom settings postgresql."""
    cursor = connection.cursor()
    if value:
        value = six.text_type(value)
    else:
        value = u''

    sql = u"SELECT set_config(%s, %s, False);"
    cursor.execute(sql, (key, value))


def get_ip(request):
    u"""Возвращает ip источника запроса.

    :param request: запрос
    :type django.http.HttpRequest

    :return IP адрес
    :rtype str or None
    """
    assert isinstance(request, HttpRequest), type(request)

    # Берем ip из X-Real-IP, если параметр установлен.
    # Вернет адрес первого недоверенного прокси.
    http_x_real_ip = request.META.get('HTTP_X_REAL_IP', None)
    if http_x_real_ip is not None:
        return http_x_real_ip

    # Берем первый ip из X-Forwarded-For, если параметр установлен.
    # Вернет первый адрес в цепочке прокси.
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forward_for is not None:
        x_forward_ip, _, _ = x_forward_for.partition(',')
        return x_forward_ip.strip()

    return request.META.get('REMOTE_ADDR', None)


def make_hstore_filter(field, value):
    u"""Создает lookup фильтр из строки.

    :param str field: название поля (type hstore).
    :param unicode value: значение, по которому фильтруется queryset.
    Если строка, то разбивается на отдельные слова.
    """
    result = reduce(
        and_,
        (Q(**{'%s__values__icontains' % field: x}) for x in value.split(' '))
    )
    return result


def make_name_filter(field, value):
    u"""Создает lookup фильтра по фамилии/имени/отчеству пользователя.

    :param str field: название поля ('firstname', 'surname', 'patronymic').
    :param unicode value: значение, по которому фильтруется queryset.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Employee = apps.get_model('employee', 'Employee')
    SysAdmin = apps.get_model('sysadmin', 'SysAdmin')

    result = None
    for model in (Employee, SysAdmin):
        type_id = ContentType.objects.get_for_model(model).id
        user_ids = list(
            model.objects.filter(
                **{'person__{}__icontains'.format(field): value}
            ).values_list('id', flat=True)
        )
        qobj = Q(user_id__in=user_ids, user_type_id=type_id)
        if result:
            result |= qobj
        else:
            result = qobj
    return result


class ModelRegistry(object):

    @cached_property
    def table_model(self):
        return {
            model._meta.db_table: model
            for model in apps.get_models(include_auto_created=True)
            if not (model._meta.proxy)
        }

    def get_model(self, table_name):
        return self.table_model.get(table_name)


model_registry = ModelRegistry()


def get_model_choices(excluded=None):
    u"""Список выбора для комбобокса.

    Ключ - id таблицы, отображаемое значение - name
    и verbose_name модели.
    """
    total_exclude = EXCLUDED_TABLES
    table_class = apps.get_model('audit_log', 'Table')
    if excluded:
        total_exclude += tuple(excluded)
    tables = (
        table
        for table in table_class.objects.iterator()
        if (table.schema, table.name) not in total_exclude
    )

    result = sorted(
        ((table.id, get_table_name(table)) for table in tables),
        key=lambda x: x[1]
    )

    return tuple(result)


def _get_m2m_model_fields(model):
    u"""Возвращает поля автоматически созданной m2m таблицы.

    :return Два поля типа ForeignKey или None, если таблица не
            соответствует автоматически созданной.
    """
    result = [
        field
        for field
        in model._meta.get_fields()
        if isinstance(field, related.ForeignKey)
    ]
    if len(result) == 2:
        return result


def get_table_name(table):
    u"""Возвращает имя таблицы в понятном пользователю виде."""
    model = get_model_by_table(table)
    if model:
        class_name = model.__name__
        verbose_name = model._meta.verbose_name.capitalize()
        if model._meta.auto_created:
            fields = _get_m2m_model_fields(model)
            if fields:
                names = [
                    get_related(f).parent_model._meta.verbose_name
                    for f in fields
                ]
                verbose_name = u'Связь {}, {}'.format(names[0], names[1])

        return u'{} - {}'.format(
            verbose_name,
            class_name
        )
    else:
        return table.name


def get_model_by_table(table):
    u"""Возвращает класс модели по имени таблицы."""
    assert isinstance(table, apps.get_model('audit_log', 'Table'))
    return model_registry.get_model(table.name)


def get_audit_log_context(request):
    u"""Возвращает параметры контекста журналирования изменений."""
    result = {}

    current_user = ioc.get('get_current_user')(request)
    if current_user:
        ContentType = apps.get_model('contenttypes', 'ContentType')

        result['user_id'] = current_user.id
        content_type = ContentType.objects.get_for_model(current_user)
        result['user_type_id'] = content_type.id
    else:
        result['user_id'] = result['user_type_id'] = 0

    result['ip'] = get_ip(request)

    return result
