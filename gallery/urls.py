from django.urls import path

from . import views

urlpatterns = [
    path("photos/", views.photos, name="photos"),
    path("videos/", views.videos, name="videos"),
    path("photos/<int:pk>/", views.photo_detail, name="photo-detail"),
    path("videos/<int:pk>/", views.video_detail, name="video-detail"),
]
