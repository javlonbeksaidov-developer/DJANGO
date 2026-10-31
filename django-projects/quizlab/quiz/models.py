from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Science(models.Model):
    name = models.CharField(max_length=255, verbose_name="Fan nomi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Quizs(models.Model):
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    minutes = models.IntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name="quizs")

    def __str__(self):
        return self.title

    @property
    def is_started(self):
        now = timezone.now()
        return self.start_time >= now

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizs"


class Questions(models.Model):
    question_text = models.TextField()
    quiz = models.ForeignKey(Quizs, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class QuestionVariants(models.Model):
    variant_text = models.TextField()
    question = models.ForeignKey(
        Questions, on_delete=models.CASCADE, related_name="question_variants"
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.variant_text

    class Meta:
        verbose_name = "Savol variant"
        verbose_name_plural = "Savol variantlar"


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    quiz = models.ForeignKey(Quizs, on_delete=models.CASCADE, related_name="answers")
    correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.correct_answers} ball"

    class Meta:
        verbose_name = "Javob"
        verbose_name_plural = "Javoblar"
