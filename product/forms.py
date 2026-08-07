from django import forms

from .models import Category, Product


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Product Name"}), label="Product Name")
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Enter Product Description", "rows": 4}), label="Description")
    price = forms.DecimalField(min_value=0, widget=forms.NumberInput(attrs={"placeholder": "Enter Price", "step": "0.01"}), label="Price")
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"placeholder": "Enter Quantity"}), label="Quantity")

    class Meta:
        model = Product
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Category Name"}), label="Category Name")
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Enter Category Description", "rows": 4}), label="Description")

    class Meta:
        model = Category
        fields = "__all__"