from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts_app.urls")),
    path("", include("home_app.urls")),
    path("product/", include("product_app.urls")),
    path("courses/", include("course_app.urls")),
    path('ticket/',include("ticket_app.urls")),
]
