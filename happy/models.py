""" Happy app models """

from django.db import models

class Product(models.Model):
    """ Product Model """
    CATEGORY_CHOICES = [("tincturas", "tincturas"), ("cremas", "cremas"), ("body_lotion", "body_lotion"), ("gomitas", "gomitas"), ("vapes", "vapes")]
    product = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    detail = models.CharField(max_length=255)
    ingredients = models.TextField()
    picture = models.ImageField(upload_to='products')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)

    def __str__(self):
        return self.product

class Contact(models.Model):
    """Contact model"""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    affair = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name