"""Happy app views"""
import random

from django.shortcuts import redirect, render
from .models import Contact, Product


def index(request):
    products = Product.objects.all()  
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        affair = request.POST.get("affair")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email,
                    affair=affair, message=message)
        contact.save()
    return render(request, 'happy/index.html', {'products':products})

def single_product(request,id):
    products = Product.objects.all()   
    random_products = random.sample(list(products), 4)
    try:
        product = Product.objects.get(pk=id)
        return render(request, 'happy/single_product.html',{'product':product, 'random_products':random_products[0:4]})
        # return render(request, 'happy/single_product.html',{'product':product})
    except:
        print(id)
        print(products)
        return redirect("happy:index")

