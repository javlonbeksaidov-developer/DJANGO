from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=200)
    price = models.FloatField(default=1000)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="quiz"
    )
    started = models.DateTimeField()
    minutes = models.IntegerField()

    def __str__(self):
        return self.title
