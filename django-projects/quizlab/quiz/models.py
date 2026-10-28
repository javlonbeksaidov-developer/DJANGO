from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Science(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Quizs(models.Model):
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    science = models.ForeignKey(
        Science, on_delete=models.CASCADE, related_name="science"
    )


class Questions(models.Model):
    question_text = models.TextField()
    quiz = models.ForeignKey(Quizs, on_delete=models.CASCADE, related_name="quiz")


class QuestionVariants(models.Model):
    variant_text = models.TextField()
    question = models.ForeignKey(
        Questions, on_delete=models.CASCADE, related_name="question"
    )
    is_correct = models.BooleanField(default=False)


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answer")
    quiz = models.ForeignKey(Quizs, on_delete=models.CASCADE, related_name="answer")
    correct_answers = models.IntegerField(default=0)
