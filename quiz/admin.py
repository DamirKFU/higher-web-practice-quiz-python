"""Модуль c админкой приложения quiz."""

from django.contrib import admin

from quiz.models import Category, Question, Quiz


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text',
        'quiz',
        'category',
        'difficulty',
        'correct_answer',
    )
    list_filter = ('difficulty', 'category', 'quiz')
    search_fields = ('text', 'correct_answer', 'description')

    readonly_fields = ('options',)
