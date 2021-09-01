"""Happy app views"""
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
    products = Product.objects.exclude(pk=id).order_by('?')[0:4]
    try:
        product = Product.objects.get(pk=id)
        return render(request, 'happy/single_product.html',{'product':product, 'random_products':products})
    except:
        print(id)
        print(products)
        return redirect("happy:index")

