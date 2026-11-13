from django.urls import path

from .views import (
    CategoryAddView,
    CategoryDeleteView,
    CategoryUpdateView,
    DrugAddView,
    DrugDeleteView,
    DrugUpdateView,
    IndexPage,
)

app_name = "staff"

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("drugs-add/", DrugAddView.as_view(), name="drug_add"),
    path("drug-edit/<int:pk>/", DrugUpdateView.as_view(), name="drug_edit"),
    path("drug-delete/<int:pk>/", DrugDeleteView.as_view(), name="drug_delete"),
    path("category-add/", CategoryAddView.as_view(), name="category_add"),
    path("category-edit/<int:pk>/", CategoryUpdateView.as_view(), name="category_edit"),
    path(
        "category-delete/<int:pk>/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
]
