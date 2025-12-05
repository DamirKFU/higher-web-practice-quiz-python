"""Модуль c моделями приложения quiz"""

from django.core.exceptions import ValidationError
from django.db import models

from quiz.constants import (
    MAX_LEN_ANSWER,
    MAX_LEN_CATEGORY_TITLE,
    MAX_LEN_DIFFICULTY,
    MAX_LEN_EXPLANATION,
    MAX_LEN_QUIZ_TITLE,
    MAX_LEN_STR,
    MAX_LEN_TEXT,
)
from quiz.validators import validate_options


class Category(models.Model):
    title = models.CharField(
        max_length=MAX_LEN_CATEGORY_TITLE,
        verbose_name='название категории',
    )

    class Meta:
        """meta настроки"""

        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

    def __str__(self):
        """выводит титульник"""
        return self.title[:MAX_LEN_STR]


class Quiz(models.Model):
    title = models.CharField(
        max_length=MAX_LEN_QUIZ_TITLE,
        verbose_name='название квиза',
    )

    description = models.TextField(
        max_length=MAX_LEN_TEXT,
        blank=True,
        null=True,
        verbose_name='описание квиза',
    )

    class Meta:
        """meta настроки"""

        verbose_name = 'квиз'
        verbose_name_plural = 'квизы'
        ordering = ['title']

    def __str__(self):
        """выводит титульник"""
        return self.title[:MAX_LEN_STR]


class Difficulty(models.TextChoices):
    EASY = 'easy', 'Лёгкий'
    MEDIUM = 'medium', 'Средний'
    HARD = 'hard', 'Сложный'


class Question(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name='квиз',
    )

    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        verbose_name='текст вопроса',
    )

    description = models.TextField(
        max_length=MAX_LEN_TEXT,
        blank=True,
        null=True,
        verbose_name='описание вопроса',
    )

    options = models.JSONField(
        verbose_name='варианты ответа',
        help_text='должно быть 2 или более вариантов',
        validators=[validate_options],
    )

    correct_answer = models.CharField(
        max_length=MAX_LEN_ANSWER,
        verbose_name='правильный ответ',
    )

    explanation = models.CharField(
        max_length=MAX_LEN_EXPLANATION,
        blank=True,
        null=True,
        verbose_name='объяснение ответа',
    )

    difficulty = models.CharField(
        max_length=MAX_LEN_DIFFICULTY,
        choices=Difficulty.choices,
        verbose_name='сложность',
    )

    class Meta:
        """meta настроки"""

        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ['difficulty', 'id']
        default_related_name = 'questions'

    def clean(self) -> None:
        """проверка коректности модели"""
        super().clean()

        if self.correct_answer not in self.options:
            raise ValidationError({
                'correct_answer': (
                    'Правильный ответ должен быть среди вариантов ответа.'
                )
            })

    def __str__(self):
        """выводит текст"""
        return self.text[:MAX_LEN_STR]
