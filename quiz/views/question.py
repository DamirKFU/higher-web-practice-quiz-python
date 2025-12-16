"""Модуль с контроллерами для вопросов."""

from django.http import HttpRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from quiz.models import Question
from quiz.serializers import QuestionAnswerSerializer, QuestionSerializer
from quiz.services.question import QuestionService


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API для работы с вопросами.

    Стандартные CRUD операции используют ModelViewSet напрямую.
    Нестандартные действия используют QuestionService.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    service = QuestionService()

    @action(detail=False, url_path='by_text/(?P<query>.+)', methods=['get'])
    def by_text(self, request: HttpRequest, query: str) -> Response:
        """Получение вопроса по тексту."""

        questions = self.service.get_questions_by_text(query)
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)

    @action(detail=True, url_path='check', methods=['post'])
    def check(self, request: HttpRequest, pk: str) -> Response:
        """Проверка ответа на вопрос."""

        serializer = QuestionAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.validated_data['answer']

        is_correct = self.service.check_answer(int(pk), answer)
        return Response({'correct': is_correct})
