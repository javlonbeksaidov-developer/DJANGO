from django.contrib import admin

from .models import Answers, Questions, QuestionVariants, Quizs, Science

# Register your models here.

admin.site.register(Science)
admin.site.register(Quizs)
admin.site.register(Answers)


class QuestionVariantsInline(admin.StackedInline):
    model = QuestionVariants
    extra = 1
    max_num = 5

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'quiz']  # noqa: RUF012
    inlines = [QuestionVariantsInline]  # noqa: RUF012
