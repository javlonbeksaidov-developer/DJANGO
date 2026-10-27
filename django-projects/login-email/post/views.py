from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "post/create.html")


def post_create_page(request):
    return render(request, "post/create.html")
