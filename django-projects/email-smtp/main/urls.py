from django.urls import path

from .views import home_page, send_html_email, send_message

app_name = "main"

urlpatterns = [
    path("", home_page, name="home"),
    path("email/", send_message, name="send_message"),
    path("email_html", send_html_email, name="send_html_email"),
]
