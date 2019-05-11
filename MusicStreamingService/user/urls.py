from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:id_user>/', views.display_user, name="display_user"),
]