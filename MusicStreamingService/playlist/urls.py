from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_playlist>/', views.display_playlist, name="display_playlist"),
]