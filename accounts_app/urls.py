from django.urls import path
from . import views


urlpatterns = [
    path("info", views.info),
    path('add', views.add_profile),
    path("list", views.userlist),
]
