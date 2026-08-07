from django.shortcuts import render
from .models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = '/users/'
    # template_name = 'user/user_form.html'

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserForm
    success_url = '/users/'

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model= User
    success_url = '/users/'