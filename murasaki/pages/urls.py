from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("news/", views.news, name="news"),
    path("tour/", views.tour, name="tour"),
    path("music/", views.music, name="music"),
    path("band/", views.band, name="band"),
]