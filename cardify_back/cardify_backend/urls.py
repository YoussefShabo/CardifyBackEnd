from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cardify', views.cardify_view.as_view(), name="cardify_view"),
]