from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("news/", views.news, name="news"),
    path("news/<int:pk>/", views.news_detail, name="news-detail"),
    path("tour/", views.tour, name="tour"),
    path("tour/<int:pk>/", views.tour_detail, name="tour-detail"),
    path("music/", views.music, name="music"),
    path("band/", views.band, name="band"),
]