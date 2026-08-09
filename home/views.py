from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import redirect, render

from order.models import Order

from .forms import UserSignUpForm


def login_view(request):
    return render(request, "home/login.html")


def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("home:login")
    else:
        form = UserSignUpForm()
    return render(request, "home/signup.html", {"form": form})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("home:login")
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    orders_by_status = Order.objects.values("status").annotate(count=Count("status"))
    status_count = {
        "pending": 0,
        "processing": 0,
        "shipped": 0,
        "delivered": 0,
        "cancelled": 0,
    }
    status_count.update({item["status"]: item["count"] for item in orders_by_status})
    context = {
        "total_users": total_users,
        "total_orders": total_orders,
        "orders_by_status": orders_by_status,
        "status_count": status_count,
    }
    return render(request, "home/dashboard.html", context)


def logout_view(request):
    logout(request)
    return redirect("home:login")