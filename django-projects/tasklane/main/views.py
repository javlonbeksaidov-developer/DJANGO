from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.


def index_page(request):
    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)
        if user is None:
            return redirect("register.html")

        login(request, user)

        return redirect("index.html")

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username, password=password, full_name=full_name
        )

        if user:
            return redirect("login.html")

    return render(request, "register.html")


def profile_page(request):
    return render(request, "profile.html")


def manage_page(request):
    return render(request, "manage.html")
