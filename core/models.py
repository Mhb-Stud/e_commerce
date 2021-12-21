from django.db import models
from user.models import *

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.FloatField(default=0)
    is_complete = models.BooleanField(default=False)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    super_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    picture = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

class OrderProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)


class ProductAttribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
