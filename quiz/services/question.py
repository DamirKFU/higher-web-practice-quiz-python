"""Модуль с реализацией сервиса вопросов."""

from django.shortcuts import get_object_or_404

from quiz.dao import AbstractQuestionService
from quiz.models import Question
from quiz.services.quiz import QuizService
from quiz.utils import update_instance


class QuestionService(AbstractQuestionService):
    """Реализация сервиса для вопросов."""

    quiz_service = QuizService()

    def list_questions(self) -> list[Question]:
        """
        Возвращает список всех вопросов.

        :return: Список вопросов.
        """
        return list(Question.objects.all())

    def get_question(self, question_id: int) -> Question:
        """
        Возвращает вопрос по его идентификатору.

        :param question_id: Идентификатор вопроса.
        :return: Вопрос из БД.
        """
        return get_object_or_404(Question, pk=question_id)

    def get_questions_by_text(self, text: str) -> list[Question]:
        """
        Возвращает вопрос по его тексту.

        :param text: Текст вопроса.
        :return: Вопрос из БД.
        """
        return list(Question.objects.filter(text__icontains=text))

    def get_questions_for_quiz(self, quiz_id: int) -> list[Question]:
        """
        Получение вопросов по идентификатору квиза.

        :param quiz_id: Идентификатор квиза.
        :return: Список вопросов квиза.
        """
        return list(Question.objects.filter(quiz_id=quiz_id))

    def create_question(self, quiz_id: int, data: dict) -> Question:
        """
        Создает новый вопрос.

        :param quiz_id: Идентификатор квиза, к которому относится вопрос.
        :param data: Данные из запроса для создания вопроса.
        :return: Созданный вопрос.
        """
        data['quiz_id'] = quiz_id
        return Question.objects.create(**data)

    def update_question(self, question_id: int, data: dict) -> Question:
        """
        Обновляет существующий вопрос.

        :param question_id: Идентификатор вопроса.
        :param data: Данные для обновления вопроса.
        :return: Обновленный вопрос.
        """
        return update_instance(Question, question_id, data)

    def delete_question(self, question_id: int) -> None:
        """
        Удаляет вопрос по его идентификатору.

        :param question_id: Идентификатор вопроса для удаления.
        """
        get_object_or_404(Question, pk=question_id).delete()

    def check_answer(self, question_id: int, answer: str) -> bool:
        """
        Проверяет ответ на вопрос.

        :param question_id: Идентификатор вопроса.
        :param answer: Ответ пользователя.
        :return: True, если ответ правильный, False - в противном случае.
        """
        return Question.objects.filter(
            pk=question_id,
            correct_answer=answer,
        ).exists()

    def random_question_from_quiz(self, quiz_id: int) -> Question:
        """
        Возвращает случайный вопрос из указанного квиза.

        :param quiz_id: Идентификатор квиза.
        :return: Случайный вопрос из квиза.
        """
        return (
            self.quiz_service.get_quiz(
                quiz_id,
            )
            .questions
            .order_by('?')
            .first()
        )
