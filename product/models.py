from django.db import models



# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "products"
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name