"""Модуль c роутингом"""


#### Category

# - POST `/api/category` - создание категории
# - GET `/api/category` - получение всех категории
# - GET `/api/category/<int:id>` - получение категории по идентификатору
# - PUT `/api/category/<int:id>` - изменение категории
# - DELETE `/api/category/<int:id>` - удаление категории


#### Question

# - POST `/api/question` - создание вопроса
# - GET `/api/question` - получение всех вопросов
# - GET `/api/question/<int:id>` - получение вопроса по идентификатору
# - GET `/api/question/by_text/<str:text>` - получение вопроса по тексту
# - POST `/api/question/<int:id>/check` - проверка ответа на вопрос
# - PUT `/api/question/<int:id>` - изменение вопроса
# - DELETE `/api/question/<int:id>` - удаление вопроса


#### Quiz

# - POST `/api/quiz` - создание квиза
# - GET `/api/quiz` - получение всех квизов
# - GET `/api/quiz/<int:id>` - получение квиза по идентификатору
# - GET `/api/quiz/<int:id>/random_question` - получение случайного вопроса по идентификатору квиза
# - GET `/api/quiz/by_title/<str:title>` - получение квиза по названию
# - PUT `/api/quiz/<int:id>` - изменение квиза
# - DELETE `/api/quiz/<int:id>` - удаление квиза


# Сюда добавляем все пути и их обработчики
urlpatterns = []
