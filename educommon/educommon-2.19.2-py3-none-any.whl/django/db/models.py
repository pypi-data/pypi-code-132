# coding: utf-8
from __future__ import absolute_import

from django.db import models
from m3.actions.exceptions import ApplicationLogicException
from m3.db import BaseObjectModel

from .mixins import DeferredActionsMixin
from .mixins import DeleteOnSaveMixin
from .mixins import StringFieldsCleanerMixin
from .mixins.validation import ModelValidationMixin


class BaseModel(
    DeferredActionsMixin,
    DeleteOnSaveMixin,
    StringFieldsCleanerMixin,
    ModelValidationMixin,
    BaseObjectModel
):

    u"""Базовый класс для всех моделей системы."""

    class Meta:
        abstract = True


class ReadOnlyMixin(models.Model):

    u"""Класс-примесь для моделей с записями только для чтения.

    В основной модели должны быть реализованы два метода:
        - is_read_only()
        - get_read_only_error_message(delete)

    is_read_only(obj) должен возаращать True, если объект модели obj не
    подлежит изменению/удалению.

    get_read_only_error_message(delete=False) должен возвращать текст сообщения
    об ошибке. Параметр delete определяет операцию (False - изменение, True -
    удаление).
    """
    def _check_read_only(self, delete):
        if self.is_read_only():
            raise ApplicationLogicException(
                self.get_read_only_error_message(delete=delete)
            )

    def safe_delete(self, *args, **kwargs):
        self._check_read_only(delete=True)

        return super(ReadOnlyMixin, self).safe_delete(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self._check_read_only(delete=True)

        super(ReadOnlyMixin, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self._check_read_only(delete=False)

        super(ReadOnlyMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True
