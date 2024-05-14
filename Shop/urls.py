from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts_app.urls")),
    path("", include("home_app.urls")),
]
