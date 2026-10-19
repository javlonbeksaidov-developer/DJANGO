from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import *

# Create your views here.


def index_1(request):
    contact_info = ContactInfo.objects.first()
    # categories = Category.objects.all()
    posts = Post.objects.all()
    owner = User.objects.get(id=1)
    data = {
        "posts": posts,
        "owner": owner,
        "contact_info": contact_info,
        # "categories": categories,
    }
    return render(request, "index.html", context=data)


def index_2(request):
    contact_info = ContactInfo.objects.first()
    # categories = Category.objects.all()
    posts = Post.objects.all()
    owner = User.objects.get(id=1)
    data = {
        "posts": posts,
        "owner": owner,
        "contact_info": contact_info,
        # "categories": categories,
    }
    return render(request, "index-2.html", context=data)


def about(request):
    owner = User.objects.get(id=1)
    data = {"owner": owner}
    return render(request, "about.html", context=data)


def contact(request):
    contact_info = ContactInfo.objects.first()
    data = {
        "contact_info": contact_info,
    }

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        new_contact = Contact.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        new_contact.save()

    return render(request, "contact.html", context=data)


def fashion(request):
    contact_info = ContactInfo.objects.first()
    owner = User.objects.get(id=1)
    # categories = Category.objects.all()
    posts = Post.objects.all()[:6]
    popular_articles = Post.objects.all()[:3]

    data = {
        "owner": owner,
        # "categories": categories,
        "posts": posts,
        "popular_articles": popular_articles,
        "contact_info": contact_info,
    }

    if request.method == "POST":
        email = request.POST.get("email")
        new_subsribe = Subsribe.objects.create(email=email)
        new_subsribe.save()

    return render(request, "fashion.html", context=data)


def travel(request):
    contact_info = ContactInfo.objects.first()
    # categories = Category.objects.all()
    posts = Post.objects.all()
    popular_posts = Post.objects.all()[:3]
    travel_into = TravelIntro.objects.all()
    data = {
        "travel_intos": travel_into,
        "posts": posts,
        "popular_posts": popular_posts,
        # "categories": categories,
        "contact_info": contact_info,
    }
    return render(request, "travel.html", context=data)


def photography(request):
    contact_info = ContactInfo.objects.first()
    # categories = Category.objects.all()
    posts = Post.objects.all()
    data = {
        "posts": posts,
        "contact_info": contact_info,
        # "categories": categories,
    }
    return render(request, "photography.html", context=data)


def register(request):
    if request.method == "POST":
        new_user = User.objects.create_user(
            username=request.POST.get("username"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            password=request.POST.get("password"),
            is_staff=True,
            is_superuser=True,
        )
        new_user.save()

        return redirect("elen:login")

    return render(request, "register.html")


def login_(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return redirect("elen:login")

        login(request, user)
        return redirect("/admin/")

    return render(request, "login.html")
