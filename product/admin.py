from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at', 'expiry_date','price','quantity','category')
    search_fields = ('name','id','price')
    list_filter = ('created_at', 'expiry_date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)