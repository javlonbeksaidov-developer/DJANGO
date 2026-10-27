from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)
        if user is None:
            messages.error(request, message="Username or password is wrong !")
            return redirect("auth_app:login")

        login(request=request, user=user)
        return redirect("main:home")

    return render(request, "auth_app/login.html")


def logout_page(request):
    logout(request)
    return redirect("auth_app:login")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user.save()

        if user:
            return redirect("auth_app:login")

    return render(request, "auth_app/register.html")

def profile_page(request):
    return render(request, "auth_app/profile.html")

def password_change_page(request):
    return render(request, "auth_app/password_change.html")