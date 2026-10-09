from django.shortcuts import render

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
