# coding: utf-8
u"""Кастомные поля моделей Django"""
from datetime import datetime
from datetime import timedelta

from django.core import validators
from django.db.models import fields
from objectpack import IMaskRegexField

from educommon.django.db.migration import date_difference_as_callable
from educommon.django.db.validators import simple
from educommon.extjs.fields import input_params
from educommon.utils.misc import cached_property


__all__ = [
    u'SingleErrorDecimalField',
    u'FIOField',
    u'RangedDateField',
    u'LastNameField',
    u'FirstNameField',
    u'MiddleNameField',
    u'SNILSField',
    u'BirthDateField',
    u'DocumentSeriesField',
    u'DocumentNumberField',
    u'PassportSeriesField',
    u'PassportNumberField',
    u'INNField',
    u'KPPField',
    u'OGRNField'
]


class SingleErrorDecimalField(fields.DecimalField):

    u"""
    Кастомный класс поля Decimal.

    Переопределяется метод validators для подключения
    SingleErrorDecimalValidator который приводит сообщение об ошибке к единому
    стилю не разделя ошибки по переполнению целой + дробной части и отдельно
    целой.
    """

    @cached_property
    def validators(self):
        u"""
        Переопрелеление стандартного валидатора Decimal.

        :return: Список валидаторов.
        """
        validators = super(SingleErrorDecimalField, self).validators
        validators.pop()
        validators.append(
            simple.SingleErrorDecimalValidator(
                self.max_digits, self.decimal_places
            )
        )
        return validators


class FIOField(fields.CharField, IMaskRegexField):
    _mask_re = r'^[а-яА-ЯёЁa-zA-Z\s-]*$'

    default_validators = [
        simple.FIOValidator()
    ]


class RangedDateField(fields.DateField):
    u"""Поле, реализующее валидаторы по умолчанию для границ периода"""
    def __init__(self, minimum_date=datetime(1917, 1, 1).date(),
                 maximum_date=None, **kwargs):
        super(RangedDateField, self).__init__(**kwargs)
        self.validators.append(simple.date_range_validator(
            minimum=minimum_date, maximum=maximum_date))


class LastNameField(FIOField):
    """Расширение поля ФИО для фамилии"""
    def __init__(self, verbose_name=u'Фамилия', max_length=30, **kwargs):
        super(LastNameField, self).__init__(
            verbose_name=verbose_name, max_length=max_length, **kwargs)


class FirstNameField(FIOField):
    """Расширение поля ФИО для имени"""
    def __init__(self, verbose_name=u'Имя', max_length=30, **kwargs):
        super(FirstNameField, self).__init__(
            verbose_name=verbose_name, max_length=max_length, **kwargs)


class MiddleNameField(FIOField):
    """Расширение поля ФИО для отчества"""
    def __init__(self, verbose_name=u'Отчество',
                 null=True, blank=True, max_length=30, **kwargs):
        super(MiddleNameField, self).__init__(
            verbose_name=verbose_name, null=null, blank=blank,
            max_length=max_length, **kwargs)


class SNILSField(fields.CharField, IMaskRegexField):
    _mask_re = r'^[-\s\d]{0,14}$'

    default_validators = [
        simple.SNILSValidator()
    ]

    def __init__(
        self, verbose_name=u'СНИЛС', **kwargs
    ):
        kwargs.setdefault('max_length', 14)
        super(SNILSField, self).__init__(
            verbose_name=verbose_name, **kwargs)


class BirthDateField(RangedDateField):
    def __init__(self, minimum_date=datetime(1917, 1, 1).date(),
                 maximum_date=date_difference_as_callable(timedelta(days=1)),
                 verbose_name=u'Дата рождения', **kwargs):
        super(BirthDateField, self).__init__(
            minimum_date=minimum_date, maximum_date=maximum_date,
            verbose_name=verbose_name, **kwargs)


class DocumentSeriesField(fields.CharField, IMaskRegexField):
    _mask_re = r'^[a-zA-Zа-яА-ЯёЁ\d\s|\-|\.|\,|\\|\/]*$'

    default_validators = [
        simple.DocumentSeriesValidator()
    ]

    def __init__(
        self, verbose_name=u'Серия документа', **kwargs
    ):
        super(DocumentSeriesField, self).__init__(
            verbose_name=verbose_name, **kwargs)


class DocumentNumberField(fields.CharField, IMaskRegexField):
    _mask_re = r'^[a-zA-Zа-яА-ЯёЁ\d\s|\-|\.|\,|\\|\/]*$'

    default_validators = [
        simple.DocumentNumberValidator()
    ]

    def __init__(
        self, verbose_name=u'Номер документа', **kwargs
    ):
        super(DocumentNumberField, self).__init__(
            verbose_name=verbose_name, **kwargs)


class PassportSeriesField(DocumentSeriesField):
    _mask_re = r'^\d{0,4}$'

    default_validators = [
        simple.PassportSeriesValidator()
    ]

    def __init__(
        self, verbose_name=u'Серия паспорта', **kwargs
    ):
        kwargs.setdefault('max_length', 4)
        super(PassportSeriesField, self).__init__(
            verbose_name=verbose_name, **kwargs)


class PassportNumberField(DocumentNumberField):
    _mask_re = r'^\d{0,6}$'

    default_validators = [
        simple.PassportNumberValidator()
    ]

    def __init__(
        self, verbose_name=u'Номер паспорта', **kwargs
    ):
        kwargs.setdefault('max_length', 6)
        super(PassportNumberField, self).__init__(
            verbose_name=verbose_name, **kwargs)


class INNField(fields.CharField, IMaskRegexField):
    _mask_re = r'^\d{0,12}$'

    default_validators = [
        simple.inn_validator
    ]

    def __init__(self, verbose_name=u'ИНН', **kwargs):
        kwargs.setdefault('max_length', 12)
        super(INNField, self).__init__(verbose_name=verbose_name, **kwargs)


class KPPField(fields.CharField, IMaskRegexField):
    _mask_re = r'^\d{0,9}$'

    default_validators = [
        simple.kpp_validator
    ]

    def __init__(self, verbose_name=u'КПП', **kwargs):
        kwargs.setdefault('max_length', 9)
        super(KPPField, self).__init__(
            verbose_name=verbose_name, **kwargs)
        # из за стандартного валидатора дублируются сообщения об ошибке
        # привышения длинны поля
        try:
            self.validators.remove(
                validators.MaxLengthValidator(self.max_length)
            )
        except ValueError:
            pass


class OGRNField(fields.CharField, IMaskRegexField):
    _mask_re = r'^\d{0,15}$'

    default_validators = [
        simple.ogrn_validator
    ]

    def __init__(self, verbose_name=u'ОГРН', **kwargs):
        kwargs.setdefault('max_length', 15)
        super(OGRNField, self).__init__(verbose_name=verbose_name, **kwargs)
