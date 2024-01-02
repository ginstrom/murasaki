from django.urls import path

from . import views

urlpatterns = [
    path("photos/", views.photos, name="photos"),
    path("videos/", views.videos, name="videos"),
]
