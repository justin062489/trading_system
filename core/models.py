from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=None)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Stock"


class Order(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10)
    stock = models.ForeignKey(Stocks, default=None, null=True, blank=True, on_delete=models.CASCADE)
    quantity =  models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.stock.name

    def __unicode__(self):
        return self.stock.name

    class Meta:
        verbose_name = "Order"