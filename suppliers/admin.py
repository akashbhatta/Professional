from django.contrib import admin
from .models import Supplier
# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','address','created_at','updated_at')
    search_fields = ('name','address','email')
    list_filter = ('created_at','updated_at')
