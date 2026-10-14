from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, unique=True)
    text = models.TextField()
    image = models.ImageField(upload_to="article_images/")
    created_at = models.DateField(auto_now_add=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="articles"
    )

    def __str__(self):
        return self.title
