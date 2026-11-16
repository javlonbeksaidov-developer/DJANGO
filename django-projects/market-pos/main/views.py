from django.shortcuts import render

# from django.views.generic import TemplateView


# class HomePage(TemplateView):
#     template_name = "login.html"

def home_page(request):
    return render(request, "login.html")