from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", index_page, name="index"),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_page, name="logout"),
    path("profile/", profile_page, name="profile"),
    path("manage/", manage_page, name="manage"),

    path("task/<int:pk>/update/", task_update_page, name="task_update"),
    path("task/<int:pk>/delete/", task_delete_page, name="task_delete"),

    path("profile/update/", profile_update_page, name="profile_update"),
    path("profile/delete/", profile_delete_page, name="profile_delete"),
    path("profile/password/", profile_password_page, name="profile_password"),

    path("task/<int:pk>/toggle/", tasks_toggle_page, name="tasks_toggle")
]
