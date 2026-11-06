from django.shortcuts import render

from .form import BookCreateForm

# Create your views here.


def home_page(request):
    data = {}
    data["book_create_form"] = BookCreateForm
    return render(request, "index.html", context=data)
