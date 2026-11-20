from django.db import models



class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    barcode = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    sell_price = models.FloatField(0)
    original_price = models.FloatField(default=0)
    store_amount = models.FloatField(default=0)
    unit = models.CharField(max_length=15)
    is_archived = models.BooleanField(default=False)
    
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="prducts")

    def __str__(self):
            return self.name
        

class Discount(models.Model):
    type_discount = models.CharField(max_length=50)
    value = models.FloatField(default=0)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="discounts")
    
    def __str__(self):
            return self.id