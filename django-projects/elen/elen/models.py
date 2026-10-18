from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    image = models.ImageField(upload_to="profile_images", blank=True)
    description = models.TextField()

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.owner.username


class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=77)

    def __str__(self):
        return self.website


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="post_images/")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")

    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subsribe(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class TravelIntro(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="travel_intro_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
