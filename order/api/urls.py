from django.urls import path
from .view import OrderDetailAPIView, OrderListAPIView

app_name = "order-api"

urlpatterns = [
    path('create/', OrderListAPIView.as_view(), name="order-list"),
    path('edit-delete-get-order/<int:pk>/', OrderDetailAPIView.as_view(), name="order-detail"),
]
