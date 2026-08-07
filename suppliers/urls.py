from django.urls import path

from .views import SupplierCreateView,SupplierDeleteView, SupplierListView, SupplierUpdateView


urlpatterns = [
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/<int:pk>/update/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier-delete"),
]