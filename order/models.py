from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "Pending"
        PROCESSING = "Processing"
        SHIPPED = "shipped"
        DELIVERED = "delivered"
        CANCELLED = "cancelled"
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=None, blank=True)
    status = models.CharField(max_length=100, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    order_details = models.ManyToManyField(Product)

class Meta:
    db_table = "order"
    verbose_name = "Order"
    verbose_name_plural = "Orders"

def __str__(self):
    return f"order{self.order_id} - {self.status}"