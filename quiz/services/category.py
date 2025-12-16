"""Модуль с реализацией сервиса категорий."""

from django.shortcuts import get_object_or_404

from quiz.dao import AbstractCategoryService
from quiz.models import Category
from quiz.utils import update_instance


class CategoryService(AbstractCategoryService):
    """Реализация сервиса для категорий."""

    def list_categories(self) -> list[Category]:
        """Метод для получения списка категорий."""
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
        item, _ = Category.objects.get_or_create(title=title)
        return item

    def update_category(self, category_id: int, data: dict) -> Category:
        """
        Обновляет категорию новыми данными.

        :param category_id: Идентификатор категории.
        :param data: Данные для обновления категории.
        :return: Обновленная категория.
        """
        return update_instance(Category, category_id, data)

    def delete_category(self, category_id: int) -> None:
        """
        Удаляет категорию.

        :param category_id: Идентификатор категории для удаления.
        """
        get_object_or_404(Category, pk=category_id).delete()
