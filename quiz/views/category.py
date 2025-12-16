"""Модуль с контроллерами для категорий."""

from rest_framework import viewsets

from quiz.models import Category
from quiz.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API для работы с категориями.

    Стандартные CRUD операции используют ModelViewSet напрямую.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
