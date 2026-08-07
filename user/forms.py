from django import forms
from .models import User

class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Name"}), label="Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}), label="Password")

    class Meta:
        model = User
        fields = '__all__'