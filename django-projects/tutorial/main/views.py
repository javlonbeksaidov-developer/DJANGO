from django.shortcuts import redirect, render

from .form import BookCreateForm, QuizCreateForm
from .models import Book, Quiz

# Create your views here.


def home_page(request):
    data = {
        "book_create_form": BookCreateForm(),
        "quiz_create_form": QuizCreateForm(),
    }

    if request.method == "POST":

        form_type = request.POST.get("form_type")

        if form_type == "book":
            form = BookCreateForm(request.POST)

            if form.is_valid():
                Book.objects.create(
                    title=form.cleaned_data["title"],
                    category=form.cleaned_data["category"],
                    price=form.cleaned_data["price"],
                    description=form.cleaned_data["description"]
                )
                return redirect("main:home")

            data["book_create_form"] = form

        elif form_type == "quiz":
            form = QuizCreateForm(request.POST)

            if form.is_valid():
                Quiz.objects.create(
                    title=form.cleaned_data["title"],
                    category=form.cleaned_data["category"],
                    started=form.cleaned_data["started"],
                    minutes=form.cleaned_data["minutes"]
                )
                return redirect("main:home")

            data["quiz_create_form"] = form

    return render(request, "index.html", context=data)
