from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import *

# Create your views here.


@login_required()
def index_page(request):
    data = {}
    tasks = Tasks.objects.all()
    data["tasks"] = tasks
    return render(request, "index.html", context=data)


def tasks_toggle_page(request, pk):
    task = Tasks.objects.filter(id=pk).first()

    if request.method == "POST":
        task.status = not task.status
        task.save()

        return redirect("main:index")

    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request=request, username=username, password=password)
        if user is None:
            messages.error(request, message="Username or password is wrong !")
            return redirect("main:login")

        login(request, user)
        return redirect("main:index")

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username, password=password, first_name=full_name
        )

        if user:
            return redirect("main:login")

    return render(request, "register.html")


def logout_page(request):
    logout(request)
    return redirect("main:login")


def profile_page(request):
    return render(request, "profile.html")


def profile_update_page(request):
    current_user = request.user
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        username = request.POST.get("username")
        about = request.POST.get("about")

        current_user.first_name = first_name
        current_user.username = username
        current_user.save()

        current_user.profile.about = about
        current_user.profile.save()

        return redirect("main:profile")

    return render(request, "profile.html")


def profile_delete_page(request):
    current_user = request.user
    if request.method == "POST":
        current_user.delete()
        return redirect("main:register")

    return render(request, "profile.html")


def profile_password_page(request):
    current_user = request.user
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")

        if current_user.check_password(current_password):
            current_user.set_password(new_password)
            current_user.save()

            return redirect("main:login")

    return render(request, "profile.html")


def manage_page(request):
    data = {}

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")

        new_task = Tasks.objects.create(
            title=title, description=description, priority=priority, due_date=due_date
        )
        new_task.save()

        if new_task:
            return redirect("main:index")

    tasks = Tasks.objects.all()
    data["tasks"] = tasks

    return render(request, "manage.html", context=data)


def task_update_page(request, pk):
    task = Tasks.objects.filter(id=pk).first()
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.due_date = request.POST.get("due_date")

        task.save()
        return redirect("main:manage")

    return render(request, "index.html")


def task_delete_page(request, pk):
    task = Tasks.objects.filter(id=pk).first()
    if request.method == "POST":
        task.delete()
        return redirect("main:manage")

    return render(request, "index.html")
