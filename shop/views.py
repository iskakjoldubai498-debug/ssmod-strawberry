from django.shortcuts import render
from .models import ProductSet  # Product эмес, сиздин моделиңиз ProductSet

def home(request):
    # Башкы бет үчүн маалыматтар (эгер керек болсо)
    products = ProductSet.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def about(request):
    return render(request, 'shop/about.html')

def price(request):  # Бул жер 'price' болушу керек
    sets = ProductSet.objects.all()
    return render(request, 'shop/price.html', {'sets': sets})

def reviews(request):
    return render(request, 'shop/reviews.html')

def contact(request):
    return render(request, 'shop/contact.html')