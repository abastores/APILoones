from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class DataPrice(models.Model):
    price = models.FloatField() # Study DecimalField if it's convinience.
    date =  models.DateTimeField(auto_now=False, auto_now_add=False)
    add_date = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)