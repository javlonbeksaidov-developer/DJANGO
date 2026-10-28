from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    about = models.TextField()
    profile_image = models.ImageField(upload_to="profile_image", blank=True)
    joined_date = models.DateField(auto_now_add=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
