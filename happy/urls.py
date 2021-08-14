"""Happy app URLS"""

from django.urls import path
from . import views


app_name = "happy"
urlpatterns = [
    # Class based views
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("me", views.ProfileView.as_view(), name="profile"),
    path("index", views.index, name="index"),
    path("single_product/<int:id>", views.single_product, name="single_product")
]