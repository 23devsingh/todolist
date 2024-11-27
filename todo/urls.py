from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="list"),
    path("update_task/<str:key>", views.update_task, name="update_task"),
    path("delete_task/<str:key>", views.delete_task, name="delete_task"),
]
