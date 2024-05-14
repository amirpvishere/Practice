from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>Hello, This is homepage</h1>")

def contact_us(request):
    return HttpResponse("<h1>Hello, This is contact us page.</h1>")
