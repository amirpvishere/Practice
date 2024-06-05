from django.shortcuts import render, HttpResponse, redirect
from .models import Account


def userlist (request):
    users = Account.objects.all()
    return render(request, "accounts_app/userlist.html", context={"users": users})


def info(requset):
    return render(requset, "accounts_app/info.html",)


def add_profile(request):
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    age = request.GET.get('age')
    city = request.GET.get('city')
    username = request.GET.get('username')
    if fname and lname and age and city and username:
        Account.objects.create(username=username, city=city, age=age, first_name=fname, last_name=lname)
        return redirect("accounts/list")
    
    return render(request, "accounts_app/add_profile.html")
