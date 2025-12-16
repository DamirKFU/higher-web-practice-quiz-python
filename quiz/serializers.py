"""Модуль c сериализаторами."""

from rest_framework import serializers

from quiz.constants import MAX_LEN_ANSWER
from quiz.models import Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    class Meta:
        """Meta настроки."""

        model = Category
        fields = [
            'id',
            'title',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов."""

    class Meta:
        """Meta настроки."""

        model = Question
        fields = [
            'id',
            'quiz',
            'text',
            'description',
            'options',
            'correct_answer',
            'explanation',
            'difficulty',
        ]


class QuestionAnswerSerializer(serializers.Serializer):
    answer = serializers.CharField(
        max_length=MAX_LEN_ANSWER,
        help_text='ответ пользователя на вопрос'
    )


class QuizSerializer(serializers.ModelSerializer):
    """Сериализатор для квизов."""

    class Meta:
        """Meta настроки."""

        model = Quiz
        fields = [
            'id',
            'title',
            'description',
        ]
