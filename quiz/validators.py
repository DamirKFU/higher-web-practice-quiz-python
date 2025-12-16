"""Модуль c валидаторами."""

from django.core.exceptions import ValidationError

from quiz.constants import MAX_OPTIONS


def validate_options(value: any) -> None:
    """Проверка волидности вариантов ответа."""
    if not isinstance(value, list):
        raise ValidationError('Варианты ответа должны быть списком.')

    if len(value) < MAX_OPTIONS:
        raise ValidationError(
            f'Должно быть минимум {MAX_OPTIONS} варианта ответа.'
        )
