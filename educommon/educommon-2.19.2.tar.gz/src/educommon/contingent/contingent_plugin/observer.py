# coding: utf-8
from __future__ import absolute_import

from django.core.exceptions import ObjectDoesNotExist
from m3_django_compat import get_model
import six

from educommon.django.db.observer import ModelObserverBase
from educommon.django.db.observer import ModelOnlyObserverMixin
from educommon.django.db.observer import OriginalObjectMixin
from educommon.utils.storage import AbstractInstanceStorage


class ContingentFieldsObserver(
    OriginalObjectMixin,
    ModelObserverBase
):
    u"""Фиксирует изменения в полях моделей.

    Ссылки на измененные объекты сохраняются в модели
    :class:`ContingentModelChanged`.

    .. code-block:: python
       :caption: Пример использования

       model_fields = {
           # Отслеживаются изменения только в указанных полях модели Person.
           ('person', 'Person'): (
               'surname',
               'firstname',
               'patronymic',
           )
       }
       observer = ContingentFieldsObserver(model_fields)
    """

    def __init__(self, model_fields=None):
        super(ContingentFieldsObserver, self).__init__()

        self.model_fields = model_fields

        # флаг проверки наличия полей в описанных моделях
        self.__checked = False

    def _is_model_fields_valid(self, model_fields):
        u"""Проверяет наличие указаных полей model_fields в моделях."""
        for (app_label, model_name), fields in six.iteritems(model_fields):
            model = get_model(app_label, model_name)
            for field_name in (fields(model) if callable(fields) else fields):
                model._meta.get_field(field_name)

        self.__checked = True

        return True

    def _is_observable(self, model):
        key = model._meta.app_label, model.__name__
        return key in self.model_fields

    def observe(self, model):
        pass

    def _get_field_names(self, model):
        u"""Возвращает имена полей модели, за которыми ведется наблюдение.

        :param model: Модель.

        :rtype: Iterable
        """
        key = model._meta.app_label, model.__name__
        fields = self.model_fields.get(key, ())
        return fields(model) if callable(fields) else fields

    def _has_changes(self, original, instance):
        u"""Возвращает True, если объекты различаются.

        :param original: Объект до изменений.
        :param instance: Объект после изменений.

        :rtype: bool
        """
        if original is None:
            return True

        for field_name in self._get_field_names(instance.__class__):
            try:
                old_value = getattr(original, field_name, None)
            except ObjectDoesNotExist:
                old_value = None
            new_value = getattr(instance, field_name, None)
            if old_value != new_value:
                return True

        return False

    def _fix_changed_object(self, instance):
        u"""Фиксирует наличие изменений в объекте."""
        ContentType = get_model('contenttypes', 'ContentType')
        content_type = ContentType.objects.get_for_model(instance)

        ContingentModelChanged = get_model(
            'contingent_plugin', 'ContingentModelChanged'
        )
        ContingentModelChanged.objects.get_or_create(
            content_type=content_type,
            object_id=instance.pk,
        )

    def post_save(self, context, instance, sender, *args, **kwargs):
        if not self.__checked:
            assert self._is_model_fields_valid(self.model_fields)

        if self._has_changes(context.original, instance):
            self._fix_changed_object(instance)


class PreDeletionDataSavingObserver(
    OriginalObjectMixin, ModelOnlyObserverMixin, ModelObserverBase
):
    """Класс для перехвата и сохранения объекта модели перед удалением."""

    def __init__(self, storage, observables=None):
        """
        :param storage: Объект-наследник AbstractInstanceDataStorage, который
            будет заниматься сохранением удаляемых объектов моделей
        :type storage: AbstractInstanceStorage
        :param observables: Модели, за которыми необходимо наблюдение. Данный
            параметр можно не задавать, но в таком случае нужно будет отдельно
            добавить модели через метод observe.
        :type observables: Iterable
        """
        assert isinstance(storage, AbstractInstanceStorage)
        self._storage = storage

        super(PreDeletionDataSavingObserver, self).__init__()
        if observables:
            for model in observables:
                self.observe(model)

    def pre_delete(self, instance, context, **kwargs):
        self._storage.save(instance, context=context, **kwargs)
