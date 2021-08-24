"""Happy app URLS"""

from django.urls import path
from . import views


app_name = "happy"
urlpatterns = [
    path("index", views.index, name="index"),
    path("single_product/<int:id>", views.single_product, name="single_product")
]