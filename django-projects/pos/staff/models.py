from django.db import models

# Create your models here.


class CategoryDrugs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Drugs(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        CategoryDrugs, on_delete=models.CASCADE, related_name="drugs"
    )
    description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
