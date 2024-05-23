from django.urls import path
from . import views

urlpatterns = [
    path('', views.product),
    path("list", views.products_list)
]

