from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cardify_view, name="cardify_view"),
]