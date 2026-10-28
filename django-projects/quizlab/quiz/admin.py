from django.contrib import admin

from .models import Answers, Questions, QuestionVariants, Quizs, Science

# Register your models here.

admin.site.register(Science)
admin.site.register(Quizs)
admin.site.register(Questions)
admin.site.register(QuestionVariants)
admin.site.register(Answers)
