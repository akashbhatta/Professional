from django.shortcuts import render
from .models import Customer
from django.views.generic import CreateView, ListView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomerForm


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')
