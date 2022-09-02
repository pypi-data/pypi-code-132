# coding: utf-8
from __future__ import absolute_import

from collections import Iterable
from collections import defaultdict
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.dispatch.dispatcher import Signal
from django.utils.functional import cached_property
from m3.actions import ControllerCache
from m3_django_compat import atomic
from m3_django_compat import get_installed_apps
import six

from educommon.utils.db.postgresql import Lock

from .models import Permission


def _get_handler(handler):
    u"""Возвращает функцию-обработчик правила."""
    module, handler = handler.rsplit('.', 1)
    module = __import__(module, fromlist=[handler])
    handler = getattr(module, handler)
    return handler


def _get_app_permissions_modules():
    u"""Возвращает модули permissions из приложений системы.

    :rtype: generator
    """
    for app_name in get_installed_apps():
        try:
            yield import_module('.permissions', app_name)
        except ImportError as error:
            if 'No module named' not in error.args[0]:
                raise
            continue


def _get_actions():
    u"""Возвращает экшены системы, доступ к которым нужно проверять.

    :rtype: generator
    """
    for controller in ControllerCache.get_controllers():
        for pack in controller.get_packs():
            for action in pack.actions:
                if pack.need_check_permission or action.need_check_permission:
                    yield action


def _set_permission(permission, name, title, description, hidden):
    u"""Сохраняет разрешение в БД.

    Если разрешение отсутствует в БД, то создает его. Иначе обновляет его
    обработчик, название и дескриптор.
    """
    changed = False

    if permission is None:
        permission = Permission(
            name=name,
            title=title,
            description=description,
            hidden=hidden,
        )
        permission.full_clean()
        permission.save()
        changed = True
    elif (
        permission.title != title or
        permission.description != description or
        permission.hidden != hidden
    ):
        permission.title = title
        permission.description = description
        permission.hidden = hidden
        permission.full_clean()
        permission.save()
        changed = True

    return changed


class RBACManager(object):

    u"""Менеджер системы авторизации RBAC."""

    post_init = Signal(providing_args=('changed',))
    u"""Сигнал, отправляемый после обновления разрешений в БД.

    :param bool changed: Указывает, были ли в процессе инициализации подсистемы
        сделаны какие-либо изменения в БД (созданы, либо изменены, разрешения).
    """

    def __init__(self):
        self.partitions = defaultdict(set)  # Разделы системы
        self.groups = {}  # Группы разрешений
        self.permissions_by_name = {}
        self.permission_dependencies = defaultdict(set)
        self.permission_rules = defaultdict(list)
        self.hidden_permissions = set()

    def get_group_params(self, permission_name):
        u"""Возвращает имя и наименование группы по имени разрешения.

        :rtype: tuple
        :returns: ``(u'employee', u'Сотрудники')``
        """
        group_name = permission_name.split('/')[0]
        return group_name, self.groups[group_name]

    def get_partition_title(self, group_name):
        u"""Возвращает наименование раздела по имени группы разрешений.

        :rtype: unicode
        """
        for title, group_names in six.iteritems(self.partitions):
            if group_name in group_names:
                return title

    def _collect_partitions(self, permission_modules):
        u"""Сбор информации о разделах системы.

        Разделами системы являются объединения групп разрешений.
        """
        self.partitions.clear()

        processed_codes = set()

        for module in permission_modules:
            partitions = getattr(module, 'partitions', None)
            if partitions is None:
                continue

            for title, group_codes in six.iteritems(partitions):
                for code in group_codes:
                    assert code not in processed_codes, (
                        u'Группа разрешений "{}" уже закреплена за другим '
                        u'разделом системы.'.format(code)
                    )
                    self.partitions[title].add(code)
                    processed_codes.add(code)

    def _collect_groups(self, permission_modules):
        u"""Сбор информации о группах разрешений."""
        self.groups.clear()

        for module in permission_modules:
            groups = getattr(module, 'groups', None)
            if groups is None:
                continue

            for code, title in six.iteritems(groups):
                assert code not in self.groups, (
                    u'Группа разрешений "{}" ({}) уже описана в другом '
                    u'приложении.'.format(code, title)
                )

                self.groups[code] = title

    def _collect_permissions(self, permissions_modules):
        u"""Сбор разрешений системы."""
        self.permissions_by_name.clear()
        self.hidden_permissions.clear()

        # Сбор названий разрешений всей системы
        for action in _get_actions():
            if action.sub_permissions:
                for sub_perm, title in six.iteritems(action.sub_permissions):
                    perm_name = action.get_perm_code(sub_perm)
                    self.permissions_by_name[perm_name] = (title, u'')
            else:
                title = action.parent.sub_permissions.get(action.perm_code)
                perm_name = action.get_perm_code()
                self.permissions_by_name[perm_name] = (title, u'')

        # Заполнение параметров разрешений
        for module in permissions_modules:
            for params in getattr(module, 'permissions', []):
                if len(params) == 3:
                    name, title, description = params
                elif len(params) == 4:
                    name, title, description, hidden = params
                    if hidden:
                        self.hidden_permissions.add(name)
                else:
                    raise ValueError(
                        'Invalid permission params: ' + repr(params)
                    )

                assert name in self.permissions_by_name, (
                    'Permission {} not found'.format(name)
                )

                _title, _description = self.permissions_by_name[name]
                self.permissions_by_name[name] = (
                    title or _title,
                    description or _description or u'',
                )

    def _collect_dependencies(self, permissions_modules):
        u"""Сбор зависимостей между разрешениями."""
        self.permission_dependencies.clear()

        for module in permissions_modules:
            module_dependencies = getattr(module, 'dependencies', {})
            if callable(module_dependencies):
                module_dependencies = module_dependencies()

            for name, dependencies in six.iteritems(module_dependencies):
                assert name in self.permissions_by_name, (
                    'Permission {} not found'.format(name)
                )
                assert name not in self.hidden_permissions or all(
                    dependency in self.hidden_permissions
                    for dependency in dependencies
                ), (
                    u'Скрытые разрешения могут зависеть только от скрытых '
                    u'разрешений: ' + name
                )
                if __debug__:
                    for dependency in dependencies:
                        if name == dependency:
                            raise AssertionError(
                                'Permission {} can''t depend on itself'
                                .format(dependency)
                            )
                        if dependency not in self.permissions_by_name:
                            raise AssertionError(
                                'Permission {} not found'.format(dependency)
                            )

                self.permission_dependencies[name].update(dependencies)

    def _collect_rules(self, permissions_modules):
        u"""Сбор обработчиков правил для разрешений системы."""
        self.permission_rules.clear()

        for module in permissions_modules:
            for perm, handlers in six.iteritems(getattr(module, 'rules', {})):
                if not isinstance(handlers, Iterable):
                    handlers = [handlers]

                for handler in handlers:
                    if isinstance(handler, six.string_types):
                        handler = _get_handler(handler)
                    assert callable(handler), handler
                    self.permission_rules[perm].append(handler)

    def _update_db(self):
        u"""Обновление списка разрешений в БД на основе разрешений системы."""
        with Lock(settings.DEFAULT_DB_ALIAS, 'rbac_lock'):
            permissions_changed = False

            permissions = {
                permission.name: permission
                for permission in Permission.objects.iterator()
            }

            for params in six.iteritems(self.permissions_by_name):
                name, (title, description) = params
                changed = _set_permission(
                    permissions.get(name),
                    name,
                    title,
                    description,
                    name in self.hidden_permissions,
                )
                if changed:
                    permissions_changed = True
                self.permissions_by_name[name] = (name, title)

            self.post_init.send(sender=self, changed=permissions_changed)

    def get_dependent_permissions(self, name, _result=None):
        u"""Возвращает разрешения, от которых зависит указанное разрешение.

        :param str name: Имя разрешения.

        :rtype: set of str
        """
        if _result is None:
            primary_name = name
            _result = {name}
        else:
            primary_name = None

        for dependency in self.permission_dependencies[name]:
            if dependency not in _result:
                _result.add(dependency)
                _result.update(
                    self.get_dependent_permissions(dependency, _result)
                )

        if primary_name:
            _result.remove(primary_name)

        return _result

    @atomic
    def init(self, update_db=True):
        u"""Инициализация системы авторизации.

        1. Загружает из приложений системы списки правил и разрешений. Их поиск
           осуществляется в модуле ``permissions``.
        2. Для каждого правила и разрешения создает/обновляет запись в БД.
        3. Объекты модели ``Permission`` сохраняет в словаре
           ``self.permissions_by_name``.

        :param bool update_db: Определяет необходимость синхронизации прав
            доступа системы с БД. Если синхронизация с БД не выполняется, то в
            словаре ``permissions_by_name`` будут параметры разрешений, а не
            сами разрешения!
        """
        ControllerCache.populate()

        modules = tuple(_get_app_permissions_modules())

        # Сбор разрешений системы и зависимостей между ними
        self._collect_permissions(modules)
        self._collect_dependencies(modules)

        # Сбор обработчиков правил для разрешений системы
        self._collect_rules(modules)

        # Сбор групп разрешений и разделов системы
        self._collect_groups(modules)
        self._collect_partitions(modules)

        if update_db:
            self._update_db()

    @cached_property
    def _backend(self):
        backend_name = getattr(settings, 'RBAC_BACKEND', None) or (
            __name__.rpartition('.')[0] + '.backends.caching.CachingBackend'
        )
        module_name, class_name = backend_name.rsplit('.', 1)

        try:
            module = import_module(module_name)
        except ImportError as e:
            raise ImproperlyConfigured(
                'Error importing RBAC backend module {}: "{}"'
                .format(module_name, e)
            )

        try:
            backend_class = getattr(module, class_name)
        except AttributeError:
            raise ImproperlyConfigured(
                'Module "{}" does not define a RBAC backend "{}"'
                .format(module, class_name)
            )
        else:
            backend = backend_class(self)

        return backend

    def has_access(self, action, request):
        u"""Проверяет наличие у текущего пользователя разрешения.

        Если у пака need_check_permission равен True, то проверка прав доступа
        будет выполняться для всех экшенов этого пака вне зависимости от
        значения параметра need_check_permission у экшенов. Также проверка
        наличия разрешений будет выполняться, если у пака значение параметра
        need_check_permission равно False, но у экшена оно равно True. В
        остальных случаях метод сразу возвращает True.

        .. important::

           Проверка доступа в данном методе происходит с учетом правил,
           назначенных соответствующим разрешениям.

        :param action: Экшн, к которому проверяется наличие доступа.
        :type action: m3.actions.Action

        :param request: HTTP-запрос.
        :type request: django.http.HttpRequest

        :rtype: bool
        """
        return self._backend.has_access(action, request)

    def has_perm(self, user, perm_name):
        u"""Проверяет наличие у пользователя разрешения.

        .. important::

           Проверка доступа в данном методе происходит **без** учета правил,
           назначенных соответствующим разрешениям.

        :param user: Пользователь, возвращаемый функцией
            ioc.get('get_current_user').
        :param basestring perm_name: Имя разрешения.

        :rtype: bool
        """
        return self._backend.has_perm(user, perm_name)


rbac = RBACManager()
