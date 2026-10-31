from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Answers, QuestionVariants, Quizs, Science

# Create your views here.


class MainPage(ListView):
    template_name = "index.html"
    model = Quizs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sciences"] = Science.objects.all()

        return context

class QuizPage(DetailView):
    template_name = "quiz.html"
    model = Quizs
    context_object_name = "quiz"

class AnswerPage(View):
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
