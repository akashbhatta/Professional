from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render

from order.models import Order

from .forms import LoginForm, UserSignUpForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home:dashboard")

            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "home/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("home:login")
    else:
        form = UserSignUpForm()

    return render(request, "home/signup.html", {"form": form})


@login_required
def dashboard_view(request):
    counts = dict(Order.objects.values_list("status").annotate(total=Count("status")))
    status_count = {
        "pending": counts.get(Order.OrderStatus.PENDING, 0),
        "processing": counts.get(Order.OrderStatus.PROCESSING, 0),
        "shipped": counts.get(Order.OrderStatus.SHIPPED, 0),
        "delivered": counts.get(Order.OrderStatus.DELIVERED, 0),
        "cancelled": counts.get(Order.OrderStatus.CANCELLED, 0),
    }
    return render(request, "home/dashboard.html", {"status_count": status_count})


def logout_view(request):
    logout(request)
    return redirect("home:login")
