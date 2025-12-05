"""Модуль c роутингом"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from quiz.views.category import CategoryViewSet
from quiz.views.question import QuestionViewSet
from quiz.views.quiz import QuizViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'quiz', QuizViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
