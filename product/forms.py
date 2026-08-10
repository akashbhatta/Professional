from django import forms

from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "quantity", "category"]
        labels = {
            "name": "Product Name",
            "price": "Price",
            "quantity": "Quantity",
            "category": "Category",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Product Name"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Price", "step": "0.01"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter Quantity"}),
            "category": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Category"}),
        }


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Category Name"}), label="Category Name")
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Enter Category Description", "rows": 4}), label="Description")

    class Meta:
        model = Category
        fields = "__all__"
