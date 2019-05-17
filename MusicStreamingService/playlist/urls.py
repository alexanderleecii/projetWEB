from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_playlist>/', views.display_playlist, name="display_playlist"),
    path('addsong/', views.add_song_ajax, name="add_song_ajax"),
]