from django.shortcuts import render

from quiz.models import Quizs

from .forms import QuizCreateForm

# Create your views here.


def staff_page(request):
    data = {"quizs": Quizs.objects.all, "quiz_create_form": QuizCreateForm()}

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "quiz_creation":
            form = QuizCreateForm(request.POST)

            if form.is_valid():
                form.save()
                form = QuizCreateForm()

    return render(request, "admin.html", context=data)
