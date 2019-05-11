from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_artist>/', views.display_artist, name="display_artist"),
]