from django.shortcuts import render
from .models import Products

def product(request):
    return render(request, "product_app/product.html")


def products_list(request):
    products = Products.objects.all()
    return render(request, "product_app/products_list.html", context={"products": products})