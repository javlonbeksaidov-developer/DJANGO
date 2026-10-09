from django.urls import path

from .views import *

app_name = 'chiqim'

urlpatterns = [
    path("login/", view=login, name="login"),
    path("register/", view=register, name="register"),
    path("profile/", view=profile, name="profile"),
    path("", view=dashboard, name="dashboard"),
    path("categories/", view=categories, name="categories"),
    path("expenses/", view=expenses, name="expenses"),
    path("expense_form/", view=expense_form, name="expense_form"),
]