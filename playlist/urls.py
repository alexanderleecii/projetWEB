from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_playlist>/', views.display_playlist, name="display_playlist"),
    path('addsong/', views.add_song_ajax, name="add_song_ajax"),
    path('removesong/', views.remove_song_ajax, name="remove_song_ajax"),
    path('update/', views.update_playlist_ajax, name="update_playlist_ajax"),
    path('delete/', views.delete_playlist_ajax, name="delete_playlist_ajax"),
]