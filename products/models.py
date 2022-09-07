from tkinter.tix import Tree
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey("Category",related_name='product_category', on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
     


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'