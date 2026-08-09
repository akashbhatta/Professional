from django.urls import path

from .views import dashboard_view, login_view, logout_view, signup_view

app_name = "home"


urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("login", login_view, name="login-no-slash"),
]
