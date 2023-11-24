from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:pk>/<slug:slug>", views.detail, name="detail"),
]
