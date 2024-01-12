from django.contrib import admin
from django.urls import path, include
from . import views

app_name='category'
urlpatterns = [
    path('add/', views.add_category, name='add_category')
]