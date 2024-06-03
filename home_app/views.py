from django.shortcuts import render

def home(request):
    return render(request, "home_app/home.html")


def contact_us(request):
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    age = request.GET.get('age')
    return render(request, "home_app/contact_us.html")