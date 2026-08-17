from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import OrderForm
from .models import Order

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/order_list.html"
    context_object_name = "orders"
    paginate_by = 10
    queryset = Order.objects.select_related("customer").prefetch_related("order_details").order_by("-order_id")


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "order/create_order.html"
    success_url = reverse_lazy("order:order-list")


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order:order-list")


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("order:order-list")