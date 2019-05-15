from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('latest_playlists/', views.display_latest_playlists, name="display_latest_playlists"),
    path('latest_albums/', views.display_latest_albums, name="display_latest_albums"),
    #path('search/', views.search, name="search"),
]