from pyexpat import model
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=1000)
    payment_id = models.CharField(max_length=1000, blank=True)
    paid = models.BooleanField(default=False)