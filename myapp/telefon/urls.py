from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import index, by_electronic

# urlpatterns = [....

urlpatterns = [
    path('<int:electronic_id>/', by_electronic),
    path('', index)
]