from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from squadlife import views

urlpatterns = [
    path('', views.home),
    path('gallery', views.gal),
    path('contact', views.contact),
]
