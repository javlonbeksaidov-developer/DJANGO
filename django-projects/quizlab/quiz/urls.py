from django.urls import path

from .views import AnswerPage, MainPage, QuizPage

app_name = "quiz"

urlpatterns = [
    path("", MainPage.as_view(), name="main"),
    path("quiz/<int:pk>/", QuizPage.as_view(), name="quiz"),
    path("quiz-submit/", AnswerPage.as_view(), name="quiz_submit"),
]