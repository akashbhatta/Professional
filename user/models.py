from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True,null=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )


    class Meta:
        db_table = "users"
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return self.name
    
