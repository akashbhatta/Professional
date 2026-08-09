from django.urls import path
from .views  import CustomerCreateView,CustomerDeleteView,CustomerListView,CustomerUpdateView

urlpatterns = [
    path('customers/',CustomerListView.as_view(), name='customer-list'),
    path('customers/create/',CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/update/',CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/',CustomerDeleteView.as_view(), name='customer-delete'),
]
