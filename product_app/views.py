from django.shortcuts import render


def product(request):
    return render(request, "product_app/product.html")
