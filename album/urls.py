from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_album>/', views.display_album, name="display_album"),
]