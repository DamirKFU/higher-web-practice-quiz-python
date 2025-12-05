"""Модуль с реализацией сервиса категорий"""

from django.shortcuts import get_object_or_404

from quiz.dao import AbstractCategoryService
from quiz.models import Category


class CategoryService(AbstractCategoryService):
    """Реализация сервиса для категорий"""

    def list_categories(self) -> list[Category]:
        """Метод для получения списка категорий"""
        return list(Category.objects.all())

    def get_category(self, category_id: int) -> Category:
        """
        Метод для получения категории по идентификатору.

        :param category_id: Идентификатор категории.
        :return: Категория из БД.
        """
        return get_object_or_404(Category, pk=category_id)

    def create_category(self, title: str) -> Category:
        """
        Создает категорию вопросов.

        :param title: Название для категории.
        :return: Созданная категория.
        """
        return Category.objects.create(title=title)

    def update_category(self, category_id: int, data: dict) -> Category:
        """
        Обновляет категорию новыми данными.

        :param category_id: Идентификатор категории.
        :param data: Данные для обновления категории.
        :return: Обновленная категория.
        """
        category = get_object_or_404(Category, pk=category_id)

        for field, value in data.items():
            setattr(category, field, value)

        category.save()
        return category

    def delete_category(self, category_id: int) -> None:
        """
        Удаляет категорию.

        :param category_id: Идентификатор категории для удаления.
        """
        category = get_object_or_404(Category, pk=category_id)
        category.delete()
