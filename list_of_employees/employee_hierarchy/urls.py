from django.urls import path

from .views import show_employees



urlpatterns = [
    path('employees/', show_employees),
]