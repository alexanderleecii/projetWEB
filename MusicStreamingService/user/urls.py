from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_user>/', views.display_user, name="display_user"),
    path('<int:id_user>/created_playlists/', views.display_created_playlists, name="display_created_playlists"),
    path('<int:id_user>/saved_playlists/', views.display_saved_playlists, name="display_saved_playlists"),
    path('<int:id_user>/saved_albums/', views.display_saved_albums, name="display_saved_albums"),
    path('<int:id_user>/following/', views.display_following, name="display_following"), 
    path('<int:id_user>/followers/', views.display_followers, name="display_followers"),
    path('saveplaylist/', views.save_playlist_ajax, name="save_playlist_ajax"),
    path('unsaveplaylist/', views.unsave_playlist_ajax, name="unsave_playlist_ajax"),
    path('savealbum/', views.save_album_ajax, name="save_album_ajax"),
    path('unsavealbum/', views.unsave_album_ajax, name="unsave_album_ajax"),
    path('followuser/', views.follow_user_ajax, name="follow_user_ajax"),
    path('unfollowuser/', views.unfollow_user_ajax, name="unfollow_user_ajax"),
]