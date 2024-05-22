from django.shortcuts import render

def home(request):
    return render(request, "home_app/home.html")


def contact_us(request):
    return render(request, "home_app/contact_us.html")