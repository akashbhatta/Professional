from django import forms

from .models import Supplier


class SupplierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Supplier Name"}), label="Supplier Name")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label="Email")
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Enter Phone Number"}), label="Phone Number")
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Enter Address", "rows": 4}), label="Address")
    is_active = forms.BooleanField(required=False, label="Active")

    class Meta:
        model = Supplier
        fields = "__all__"