from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


# def index_page(request):
#     return render(request, "index.html")


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "Saidov Javlon"
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
