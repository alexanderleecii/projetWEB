from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('', views.register, name="register"),
]