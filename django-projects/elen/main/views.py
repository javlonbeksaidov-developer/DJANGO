from django.shortcuts import render

from .models import Contact

# Create your views here.


def index_1(request):
    return render(request, "index.html")


def index_2(request):
    return render(request, "index-2.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        new_contact = Contact.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        new_contact.save()

    return render(request, "contact.html")


def fashion(request):
    return render(request, "fashion.html")


def travel(request):
    return render(request, "travel.html")


def photography(request):
    return render(request, "photography.html")
