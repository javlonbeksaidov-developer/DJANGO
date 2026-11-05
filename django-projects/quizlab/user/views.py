from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import (
    DetailView,
    UpdateView,
)

from .models import Profile


class ProfilePage(LoginRequiredMixin, DetailView):
    template_name = "profile.html"
    model = Profile
    context_object_name = "profile"

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class UpdatePage(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profile.html"
    fields = ["about", "profile_image"]  # noqa: RUF012

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        user.first_name = self.request.POST.get("first_name")
        user.last_name = self.request.POST.get("last_name")
        user.email = self.request.POST.get("email")
        user.save()

        return response

    def get_success_url(self):
        return self.request.path


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)
        if user is None:
            messages.error(request, message="Username or password is wrong !")
            return redirect("user:login")

        login(request=request, user=user)
        return redirect("quiz:main")

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("user:login")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Parollar bir xil emas!")
            return redirect("user:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username band!")
            return redirect("user:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email band!")
            return redirect("user:register")

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        # User uchun Profile yaratish
        Profile.objects.create(user=user)

        messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
        return redirect("user:login")

    return render(request, "register.html")


def password_change_page(request):
    pass