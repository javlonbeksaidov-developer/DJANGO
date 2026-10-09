from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def profile(request):
    return render(request, "profile.html")


def dashboard(request):
    return render(request, "dashboard.html")


def categories(request):
    return render(request, "categories.html")


def expenses(request):
    return render(request, "expenses.html")


def expense_form(request):
    return render(request, "expense_form.html")
