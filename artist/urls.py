from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_artist>/', views.display_artist, name="display_artist"),
    path('<int:id_artist>/albums/', views.display_artist_albums, name="display_artist_albums"),
    path('<int:id_artist>/followers/', views.followers, name="artist_followers"),
    path('<int:id_artist>/appears_in_playlists/', views.artist_is_in_playlist, name="artist_is_in_playlist"),
    path('<int:id_artist>/appears_in_albums/', views.display_artist_albums_features, name="artist_is_in_album"),
    path('followartist/', views.follow_artist_ajax, name="follow_artist_ajax"),
    path('unfollowartist/', views.unfollow_artist_ajax, name="unfollow_artist_ajax"),
] 