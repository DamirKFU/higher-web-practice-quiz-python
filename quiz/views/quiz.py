"""Модуль с контроллерами для квизов"""

from django.http import HttpRequest
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from quiz.models import Quiz
from quiz.serializers import QuestionSerializer, QuizSerializer
from quiz.services.question import QuestionService
from quiz.services.quiz import QuizService


class QuizViewSet(viewsets.ModelViewSet):
    """
    API для работы с квизами:

    Стандартные CRUD операции используют ModelViewSet напрямую.
    Нестандартные действия используют QuestionService.
    """

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    quiz_service = QuizService()
    question_service = QuestionService()

    @action(detail=True, url_path='random_question', methods=['get'])
    def random_question(self, request: HttpRequest, pk: str) -> Response:
        """Получение случайного вопроса по идентификатору квиза"""

        question = self.question_service.random_question_from_quiz(int(pk))
        if not question:
            return Response(
                {'error': 'No questions found for this quiz'},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    @action(detail=False, url_path='by_title/(?P<title>.+)', methods=['get'])
    def by_title(self, request: HttpRequest, title: str) -> Response:
        """Получение квиза по названию"""

        quizzes = self.quiz_service.get_quizes_by_title(title)
        serializer = self.get_serializer(quizzes, many=True)
        return Response(serializer.data)
