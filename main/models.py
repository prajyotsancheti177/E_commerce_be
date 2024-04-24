from django.db import models
from django.contrib.auth.models import User

class SellerTable(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField()
    seller_phone = models.IntegerField
    seller_address = models.TextField()

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    details = models.TextField()

class ProductTable(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    seller = models.ForeignKey(SellerTable,on_delete=models.CASCADE)
