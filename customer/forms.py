from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Name"}), label="Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}), label="Password")
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter phone number"}), label="Phone")
    class Meta:
        model = Customer
        fields = '__all__'