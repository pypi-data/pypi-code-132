# coding: utf-8
"""
Внедряем в джанговский дефолтный FieldFile необходимый функционал
для работы с AtcfsStorage.
"""
from __future__ import absolute_import

import re

from django.core.files.storage import DefaultStorage
from django.core.files.storage import get_storage_class
from django.db.models.fields import files
from django.utils.encoding import smart_str
from django.utils.encoding import smart_unicode

from .storage import AtcfsStorage


DEFAULT_FILE_STORAGE = get_storage_class()


def is_atcfs_storage(storage):
    """
    Функция определяет является ли переданный storage AtcfsStorage.
    :param storage: объект Storage
    :return: True/False
    """
    # Первый случай это когда storage выставлен напрямую через параметр в филде.
    # Второй случай когда в сетингсах установлен DEFAULT_FILE_STORAGE,
    # и он не переопределен через параметр storage в филде.
    if (
        isinstance(storage, AtcfsStorage) or
        isinstance(storage, DefaultStorage) and
            DEFAULT_FILE_STORAGE == AtcfsStorage
    ):
        return True
    return False


# Переопределяем __init__ FieldFile.
# Необходимо установить field_name,
# в котором будет храниться реальное название файла.

uuid_re = re.compile(
    r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
)

old_field_file__init__ = files.FieldFile.__init__

def new_field_file__init__(self, instance, field, name):
    old_field_file__init__(self, instance, field, name)
    if is_atcfs_storage(self.storage):
        if self.name and uuid_re.match(self.name):
            self.file_name = self.storage.name(self.name)
        else:
            self.file_name = u''

files.FieldFile.__init__ = new_field_file__init__


# Переопределяем __str__ FieldFile.

old_field_file__str__ = files.FieldFile.__str__

def new_field_file__str__(self):
    if is_atcfs_storage(self.storage):
        return smart_str(self.file_name or '')
    else:
        return old_field_file__str__(self)

files.FieldFile.__str__ = new_field_file__str__


# Переопределяем __unicode__ FieldFile.

old_field_file__unicode__ = files.FieldFile.__unicode__

def new_field_file__unicode__(self):
    if is_atcfs_storage(self.storage):
        return smart_unicode(self.file_name or u'')
    else:
        return old_field_file__unicode__

files.FieldFile.__unicode__ = new_field_file__unicode__


# Переопределяем get_prep_value FileField.

old_file_field_get_prep_value = files.FileField.get_prep_value

def new_file_field_get_prep_value(self, value):
    if is_atcfs_storage(self.storage):
        if value is None:
            return None
        return value.name
    else:
        return old_file_field_get_prep_value(self, value)

files.FileField.get_prep_value = new_file_field_get_prep_value
