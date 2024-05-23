from django.shortcuts import render,HttpResponse
from .models import Account


def userlist (request):
    users = Account.objects.all()
    return render(request, "accounts_app/userlist.html", context={"users": users})


def info(requset):
    return render(requset, "accounts_app/info.html",)
