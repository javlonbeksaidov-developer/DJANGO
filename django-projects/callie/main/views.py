from django.shortcuts import render

from .models import Post

# Create your views here.


def home_page(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index-2.html")


def about(request):
    return render(request, "about.html")


def author(request):
    return render(request, "author.html")


def blank(request):
    return render(request, "blank.html")


def category(request):
    return render(request, "category.html")


def contact(request):
    return render(request, "contact.html")


def blog_post(request):
    return render(request, "blog-post.html")


def form(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }
        print(data)

    return render(request, "form.html")


def post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        category = request.POST.get("category")

        new_post = Post.objects.create(title=title, description=desc, category=category)
        new_post.save()

    return render(request, "post.html")
