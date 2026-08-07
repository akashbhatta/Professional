from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

class Meta:
    db_table = "supplier"
    verbose_name = "Supplier"
    verbose_name_plural = "Suppliers"
    # db_indexes =[
    #     models.Index(fields=['name']),
    #     models.Index(fields=['email'])
    # ]

def __str__(self):
    return self.name    
    