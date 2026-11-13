from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import DrugsAddForm
from .models import CategoryDrugs, Drugs


class IndexPage(ListView):
    template_name = "staff_page/index.html"
    model = Drugs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ctgs"] = CategoryDrugs.objects.all()
        return context


class DrugAddView(CreateView):
    model = Drugs
    form_class = DrugsAddForm
    template_name = "staff_page/add.html"
    success_url = reverse_lazy("staff:index")


class CategoryAddView(CreateView):
    model = CategoryDrugs
    fields = ["name", "description"]  # noqa: RUF012
    template_name = "staff_page/add.html"
    success_url = reverse_lazy("staff:index")


class CategoryUpdateView(UpdateView):
    model = CategoryDrugs
    fields = ["name", "description"]  # noqa: RUF012
    template_name = "staff_page/edit.html"
    success_url = reverse_lazy("staff:index")


class DrugUpdateView(UpdateView):
    model = Drugs
    form_class = DrugsAddForm
    template_name = "staff_page/edit.html"
    success_url = reverse_lazy("staff:index")


class CategoryDeleteView(DeleteView):
    model = CategoryDrugs
    template_name = "staff_page/delete.html"
    success_url = reverse_lazy("staff:index")


class DrugDeleteView(DeleteView):
    model = Drugs
    template_name = "staff_page/delete.html"
    success_url = reverse_lazy("staff:index")
