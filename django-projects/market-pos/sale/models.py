from django.contrib.auth.models import User
from django.db import models

from store.models import Products


class Check(models.Model):
    payment_type = models.CharField(max_length=10)
    sold = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="checks")

    def total(self):
        sum_ = sum([i.total() for i in self.check_items.all()])
        return sum_


class CheckItem(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="items"
    )
    amount = models.FloatField(default=0)

    check_items = models.ForeignKey(
        Check, on_delete=models.CASCADE, related_name="check_items"
    )

    def total(self):
        return 56
