# coding: utf-8
u"""Утилиты для работы с элементами управления (интерфейсами)."""
from __future__ import absolute_import

from datetime import datetime
from datetime import time
import inspect
import os

from django.conf import settings
from django.db.models import TextField
from django.db.models import Q
from m3.actions.context import ActionContext
from m3_ext.ui import all_components as ext
from m3_ext.ui.icons import Icons
from m3_ext.ui.panels.grids import ExtObjectGrid
from objectpack.filters import CustomFilter
from objectpack.filters import FilterByField as _FilterByField
from objectpack.tools import modify
from objectpack.tree_object_pack.ui import BaseObjectTree
from objectpack.ui import BaseEditWindow
from objectpack.ui import _create_control_for_field
from objectpack.ui import anchor100 as obj_anchor100
from objectpack.ui import deny_blank as obj_deny_blank
from objectpack.ui import make_combo_box

from educommon import ioc
from educommon.utils.misc import cached_property


def anchor100(*elements):
    u"""Установка anchor='100%' для перечня компонент."""
    return list(
        obj_anchor100(element)
        for element in elements
    )


def deny_blank(*elements):
    u"""Установка allow_blank=False для перечня компонент."""
    return list(
        obj_deny_blank(element)
        for element in elements
    )


def make_button(title, icon_cls, event, client_id):
    u"""Создает кнопку, оповещающую компонент с client_id на событие event."""
    handler = "function() {Ext.getCmp('%s').fireEvent('%s');}" % (
        client_id, event)

    return ext.ExtButton(text=title, icon_cls=icon_cls, handler=handler)


def formed(ctl, width=-1, label_width=100, **kwargs):
    u"""Возращает control в контейнере."""
    cont = ext.ExtContainer(layout='form')
    cont.items.append(ctl)
    ctl.anchor = '100%'
    if width > 0:
        cont.width = width
    else:
        cont.flex = -width
    cont.label_width = label_width
    cont.anchor = '100%'
    return modify(cont, **kwargs)


class ChoicesFilter(CustomFilter):
    u"""Колоночный фильтр с выпадающим списком."""

    def __init__(self, choices, *args, **kwargs):
        u"""Метод инициализации.

        Добавляем значения для выбора и тип компонента.
        """
        self._choices = choices
        kwargs['xtype'] = 'combo'

        super(ChoicesFilter, self).__init__(*args, **kwargs)

    def get_script(self):
        u"""Генерация кода компонента."""
        if callable(self._choices):
            choices = self._choices()
        else:
            choices = self._choices
        control = make_combo_box(data=list(choices))
        control._put_config_value('filterName', self._uid)
        control._put_config_value('tooltip', self._tooltip or control.label)
        control.name = self._uid
        control.allow_blank = True
        control.hide_clear_trigger = False
        control.value = None
        return [control.render()]


class ColumnFilterWithDefaultValue(_FilterByField):

    def get_script(self):
        control = _create_control_for_field(
            self.field,
            **self._field_fabric_params
        )
        control._put_config_value('filterName', self._uid)
        control._put_config_value('tooltip', self._tooltip or control.label)
        control.name = self._uid
        control.allow_blank = True
        control.hide_clear_trigger = False
        # Закомментировано, чтобы проставлять значение по-умолчанию
        # control.value = None
        return [control.render()]


def reconfigure_grid_by_access(grid, can_add=False, can_edit=False,
                               can_delete=False, can_view=True):
    u"""Перенастраивает грид в зависимости от прав доступа.

    :param grid: Перенастраиваемый грид.
    :type grid: m3_ext.ui.panels.grids.ExtObjectGrid

    :param bool can_add: Определяет доступность функции добавления объектов.
    :param bool can_edit: Определяет доступность функции изменения объектов.
    :param bool can_delete: Определяет доступность функции удаления объектов.
    :param bool can_view: Определяет доступность функции просмотра объектов.
        Используется только в случае недоступности функции изменения объектов.
    """
    assert isinstance(grid, ExtObjectGrid), type(grid)
    grid.read_only = False
    if not can_add:
        grid.url_new = None
    if not can_edit:
        if can_view:
            grid.top_bar.button_edit.text = u'Просмотр'
            grid.top_bar.button_edit.icon_cls = Icons.APPLICATION_VIEW_DETAIL

            grid.top_bar.items.remove(grid.top_bar.button_edit)
            grid.top_bar.items.insert(0, grid.top_bar.button_edit)
        else:
            grid.url_edit = None
    if not can_delete:
        grid.url_delete = None


def reconfigure_object_tree_by_access(grid, can_add=False, can_edit=False,
                                      can_delete=False, can_view=True):
    u"""Перенастраивает древовидный грид в зависимости от прав доступа.

    :param grid: Перенастраиваемый грид.
    :type grid: objectpack.tree_object_pack.ui.BaseObjectTree

    :param bool can_add: Определяет доступность функции добавления объектов.
    :param bool can_edit: Определяет доступность функции изменения объектов.
    :param bool can_delete: Определяет доступность функции удаления объектов.
    :param bool can_view: Определяет доступность функции просмотра объектов.
        Используется только в случае недоступности функции изменения объектов.
    """
    assert isinstance(grid, BaseObjectTree), type(grid)

    if not can_add:
        grid.action_new = None
    if not can_edit:
        if can_view:
            grid.top_bar.button_edit.text = u'Просмотр'
            grid.top_bar.button_edit.icon_cls = Icons.APPLICATION_VIEW_DETAIL
        else:
            grid.action_edit = None
    if not can_delete:
        grid.action_delete = None


class FilterByField(_FilterByField):

    u"""FilterByField c возможностью расширения контрола фильтра.

    Дополнительно добавляет ActionContext, необходимый в случае если
    контролом является ExtDictSelectField.
    """

    def __init__(self, *args, **kwargs):
        self._control_creator = kwargs.pop('control_creator', None)
        parser = kwargs.pop('parser_map', None)
        if parser:
            self.parsers_map = list(self.parsers_map)
            self.parsers_map.append(parser)
        super(FilterByField, self).__init__(*args, **kwargs)

    def create_control(self):
        if self._control_creator is not None:
            return self._control_creator()

        return _create_control_for_field(
            self.field,
            **self._field_fabric_params
        )

    def get_control(self):
        control = self.create_control()
        control.action_context = ActionContext()
        control._put_config_value('filterName', self._uid)
        control._put_config_value('tooltip', self._tooltip or control.label)
        control.name = self._uid
        control.allow_blank = True
        control.hide_clear_trigger = False
        return control

    def get_script(self):
        return [self.get_control().render()]


class DatetimeFilterCreator(object):

    u"""Класс, создающий колоночный фильтр по интервалу для datetime поля.

    Поддерживает значения по умолчанию.
    """

    def __init__(self, model, field_name,
                 get_from=lambda: None, get_to=lambda: None):
        u"""Фильтр по интервалу для datetime поля.

        :param django.db.models.Model model: модель для фильтра.
        :param str field_name: имя поля модели.
        :param callable get_from: возвращает дату по умолчанию для фильтра "С".
        :param callable get_to: возвращает дату по умолчанию для фильтра "По".

        Значения по умолчанию передаются в качестве callable, чтобы они
        вычислялись во время создания js. То есть, если в фильтре должна быть
        текущая дата, а пак с колонками был создан вчера, пользователь увидит
        в фильтре сегодняшнюю дату, а не вчерашнюю.
        """
        self.model = model
        self.field_name = field_name

        assert callable(get_from)
        assert callable(get_to)
        self.defaults = {
            'from': get_from,
            'to': get_to,
        }

    @cached_property
    def filter(self):
        u"""Фильтр для колонки.

        :return Группа колоночных фильтров для грида
        :rtype objectpack.filters.FilterGroup
        """
        observer = ioc.get('observer')

        return (
            FilterByField(
                self.model,
                model_register=observer,
                control_creator=lambda: ext.ExtDateField(
                    value=self.defaults['from']()
                ),
                field_name=self.field_name,
                lookup=lambda dt: Q(**{
                    self.field_name + '__gte': datetime.combine(dt, time(0))
                }),
                tooltip=u'С',
            ) & FilterByField(
                self.model,
                model_register=observer,
                control_creator=lambda: ext.ExtDateField(
                    value=self.defaults['to']()
                ),
                field_name=self.field_name,
                lookup=lambda dt: Q(**{
                    self.field_name + '__lte': datetime.combine(
                        dt, time(
                            hour=23, minute=59, second=59, microsecond=999999
                        )
                    )
                }),
                tooltip=u'По',
            )
        )

    @property
    def base_params(self):
        u"""Базовые параметры для store грида.

        :rtype: dict
        """
        result = {}

        value = self.defaults['from']()
        if value is not None:
            result[self.filter._items[0]._uid] = str(value)

        value = self.defaults['to']()
        if value is not None:
            result[self.filter._items[1]._uid] = str(value)
        return result


def switch_window_in_read_only_mode(window):
    u"""Переводит окно редактирования в режим "Только для чтения".

    Удаляет кнопку "Сохранить", на кнопке "Отмена" меняет текст на "Закрыть".

    :param window: Окно редактирования.
    :type window: :class:`objectpack.ui.BaseEditWindow`
    """
    assert isinstance(window, BaseEditWindow), type(window)

    if window.title.endswith(u': Редактирование'):
        window.title = window.title[:-len(u'Редактирование')] + u'Просмотр'

    window.buttons.remove(window.save_btn)
    window.cancel_btn.text = u'Закрыть'


def local_template(file_name):
    u"""Возвращает абсолютный путь к файлу относительно модуля.

    Основное предназначение -- формирование значений полей ``template`` и
    ``template_globals`` окон, вкладок и других компонент пользовательского
    интерфейса в тех случаях, когда файл шаблона размещен в той же папке, что
    и модуль с компонентом.

    :param str file_name: Имя файла.

    :rtype: str
    """
    frame = inspect.currentframe().f_back

    root_package_name = frame.f_globals['__name__'].rsplit('.', 2)[0]
    module = __import__(root_package_name)

    TEMPLATE_DIRS = set(
        path
        for config in settings.TEMPLATES
        for path in config.get('DIRS', ())
    )

    assert any(
        os.path.dirname(path) in TEMPLATE_DIRS
        for path in module.__path__
    ), (
        '{} package path must be in TEMPLATES config.'.format(module.__path__),
        TEMPLATE_DIRS,
    )

    # Путь к модулю вызывающей функции
    module_path = os.path.abspath(os.path.dirname(frame.f_globals['__file__']))

    for path in TEMPLATE_DIRS:
        if module_path.startswith(path):
            module_path = module_path[len(path) + 1:]
            break

    return os.path.join(module_path, file_name)


class FilterByTextField(FilterByField):

    """Фильтр для поля TextField, с ExtStringField в качестве контрола.

    Возвращает контрол однострочного текстового поля
    вместо многострочного (ExtTextArea),
    который используется по умолчанию для TextField.
    """

    def create_control(self):
        # Работаем только с TextField
        assert isinstance(self.field, TextField)

        return ext.ExtStringField(
            max_length=self.field.max_length,
            **self._field_fabric_params
        )
