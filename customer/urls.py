from django.urls import path
from .views  import CustomerCreateView,CustomerDeleteView,CustomerListView,CustomerUpdateView

urlpatterns = [
    path('customers/',CustomerListView.as_view(), name='customer-list'),
    path('customers/',CustomerDeleteView.as_view(), name='customer-delete'),
    path('customers/',CustomerCreateView.as_view(), name='customer-create'),
    path('customers/',CustomerUpdateView.as_view(), name='customer-update'),
]