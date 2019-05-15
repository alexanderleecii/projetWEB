from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_user>/', views.display_user, name="display_user"),
    path('<int:id_user>/created_playlists/', views.display_created_playlists, name="display_created_playlists"),
    path('<int:id_user>/saved_playlists/', views.display_saved_playlists, name="display_saved_playlists"),
    path('<int:id_user>/saved_albums/', views.display_saved_albums, name="display_saved_albums"),
    path('<int:id_user>/following/', views.display_following, name="display_following"), 
    path('<int:id_user>/followers/', views.display_followers, name="display_followers"),
]