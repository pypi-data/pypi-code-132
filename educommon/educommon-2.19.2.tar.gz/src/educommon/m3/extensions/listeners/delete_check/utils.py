# coding: utf-8
from __future__ import absolute_import

from django.db.models import SET_DEFAULT
from django.db.models import SET_NULL
from educommon.utils.db import get_related_fields
from m3.db import safe_delete
from m3_django_compat import get_related


def get_related_instances_and_handlers(obj, skip_func=None):
    u"""Возвращает генератор связанных объектов с функциями-обработчиками."""
    for field in get_related_fields(obj.__class__, skip_func=skip_func):
        related_model = field.model
        field_name = field.name
        if field.many_to_many:
            related_model = field.remote_field.through
            field_name = field.m2m_reverse_name()

        related_objects = related_model.objects.filter(
            **{field_name: obj}
        )

        on_delete_function = get_on_relation_delete_function(field)
        for related_obj in related_objects.iterator():
            yield related_obj, on_delete_function


def get_on_relation_delete_function(field):
    u"""Возвращает функцию, которая будет вызыватся при удалении связи.

    Если в `cascade_delete_for` модели, для поля в параметре `on_delete`
    указана функция то возвращается именно она, в противном случае
    возвращается функция, соответсвующая поведению, указанному в атрибуте
    `on_delete` поля.
    """
    return (
        get_custom_on_delete_function(field) or
        get_field_on_delete_function(field)
    )


def get_custom_on_delete_function(field):
    u"""Возвращает функцию, указанную в cascade_delete_for для поля."""
    if (
        not hasattr(field.model, 'cascade_delete_for') or
        not isinstance(field.model.cascade_delete_for, dict)
    ):
        return None
    on_delete_params = field.model.cascade_delete_for[field]
    return on_delete_params.get('on_delete')


def get_field_on_delete_function(field):
    u"""Возвращает функцию, которая соответсвует поведению on_delete поля."""
    model = field.model
    on_delete_function = get_related(field).on_delete

    if field.many_to_many:
        return safe_delete

    if on_delete_function == SET_NULL:
        def set_null(obj):
            setattr(obj, field.name, None)
            getattr(obj, 'clean_and_save', obj.save)()
        return set_null

    if on_delete_function == SET_DEFAULT:
        def set_default(obj):
            setattr(obj, field.name, field.default)
            getattr(obj, 'clean_and_save', obj.save)()
        return set_default

    # По-умолчанию остается поведение с безопасным удалением
    if hasattr(model, 'safe_delete') and callable(model.safe_delete):
        return model.safe_delete
    return safe_delete
