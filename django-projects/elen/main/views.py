from django.shortcuts import render

# Create your views here.


def index_1(request):
    return render(request, "index.html")


def index_2(request):
    return render(request, "index-2.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def fashion(request):
    return render(request, "fashion.html")


def travel(request):
    return render(request, "travel.html")


def photofgraphy(request):
    return render(request, "photofgraphy.html")
