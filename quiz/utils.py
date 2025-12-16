"""Модуль c утилитами."""

from django.db import models
from django.shortcuts import get_object_or_404


def update_instance(
    model: models.Model,
    pk: int,
    data: dict,
) -> models.Model:
    """Утилита обновления модели."""
    instance = get_object_or_404(model, pk=pk)

    for field, value in data.items():
        setattr(instance, field, value)

    instance.save()
    return instance
