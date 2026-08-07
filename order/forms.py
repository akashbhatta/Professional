from django import forms

from product.models import Product

from .models import Order


class OrderForm(forms.ModelForm):
    order_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}), label="Order Date")
    order_details = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple(), label="Products")

    class Meta:
        model = Order
        fields = "__all__"