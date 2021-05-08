from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('api/v1/register-user-details', register_visitors)
]
