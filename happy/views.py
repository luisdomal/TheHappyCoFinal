"""Users app views"""
import random
import io
import csv
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import UserForm

class LoginView(auth_views.LoginView):
    """Authenticates a user"""
    template_name = "happy/login.html"
    redirect_authenticated_user = True


class ProfileView(LoginRequiredMixin, TemplateView):
    """Shows user's profile"""
    template_name = "happy/profile.html"

class LogoutView(auth_views.LogoutView):
    """Logs out a user"""

class SignupView(FormView):
    """Register a user"""
    form_class = UserForm
    success_url = reverse_lazy("happy:profile")
    template_name = "happy/signup.html"

    def form_valid(self, form):
        """Saves a user"""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

database = []

with io.open("files/database.csv", "r", encoding="utf-8") as archivo:
  reader = csv.reader(archivo)

  for line in reader:
    database.append({
      "id": int(line[0]),
      "name": line[1],
      "price": line[2],
      "currency": line[3],
      "detail": line[4],
      "ingredients": line[5],
      "picture": line[6],
      "category": line[7]
    })

def index(request):
    products = database   
    return render(request, 'happy/index.html', {'products':products})

def single_product(request,id):
    random_products = database.copy()
    for product in database:
        if product["id"] == id:
            random.shuffle(random_products)
            return render(request, 'happy/single_product.html',{'product':product, 'random_products':random_products[0:4]})
    return redirect("happy:index")



