from django.shortcuts import render, redirect, HttpResponse
from .models import Ticket

def buy_ticket(request):
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    snumber = request.GET.get('snumber')
    if fname and lname and snumber:
        Ticket.objects.create(fname=fname, lname=lname, snumber=snumber)
        return HttpResponse("You're ticket has been reserved successfully")
    return render(request, "ticket_app/buy_ticket.html")


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "ticket_app/ticket_list.html", context={"tickets": tickets})

