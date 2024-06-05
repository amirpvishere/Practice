from django.urls import path
from . import views

urlpatterns = [
    path("buy", views.buy_ticket),
    path("list", views.ticket_list),
]