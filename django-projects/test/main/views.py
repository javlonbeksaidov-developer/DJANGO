from django.shortcuts import redirect, render

# Create your views here.


def like_it(request):
    return redirect("main:main_vedio_view")


def main_picture_view(request):
    return render(request, template_name="pictures.html")


def main_vedio_view(request):
    return render(request, template_name="vedios.html")
