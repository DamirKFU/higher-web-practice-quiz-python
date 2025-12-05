"""Модуль c валидаторами"""

from django.core.exceptions import ValidationError


def validate_options(value: any) -> None:
    """проверка волидности вариантов ответа"""

    if not isinstance(value, list):
        raise ValidationError('Варианты ответа должны быть списком.')

    if len(value) < 2:
        raise ValidationError('Должно быть минимум 2 варианта ответа.')
