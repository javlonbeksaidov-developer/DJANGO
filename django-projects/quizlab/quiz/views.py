from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Answers, QuestionVariants, Quizs, Science

# Create your views here.


class MainPage(ListView):
    template_name = "index.html"
    model = Quizs
    paginate_by = 2

    def get_queryset(self):
        data = super().get_queryset()

        title = self.request.GET.get("title")
        fan = self.request.GET.get("fan")

        if title:
            data = data.filter(title__icontains=title)

        if fan:
            data = data.filter(science__name=fan)

        return data.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sciences"] = Science.objects.all()

        return context

class QuizPage(LoginRequiredMixin, DetailView):
    template_name = "quiz.html"
    model = Quizs
    context_object_name = "quiz"

class AnswerPage(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):        
        score = 0

        for key, value in request.POST.items():
            if key.startswith("question_"):
                variant_id = value 
                
                try:
                    selected_variant = QuestionVariants.objects.get(id=variant_id)
                    if selected_variant.is_correct:
                        score += 1
                except QuestionVariants.DoesNotExist:
                    pass

        quiz_id = request.POST.get("quiz_id")
        quiz = get_object_or_404(Quizs, id=quiz_id)
        
        Answers.objects.create(
            user=request.user,
            quiz=quiz,
            correct_answers=score
        )

        return redirect("quiz:main")
