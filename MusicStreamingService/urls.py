"""MusicStreamingService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('register/', include('register.urls'), name="register_app"),
    path('login/', include('login.urls'), name="login_app"),
    path('logout/', include('logout.urls'), name="logout_app"),
    path('', include('browse.urls'), name="browse_app"),
    path('playlist/', include('playlist.urls'), name="playlist_app"),
    path('album/', include('album.urls'), name="album_app"),
    path('artist/', include('artist.urls'), name="artist_app"),
    path('user/', include('user.urls'), name="user_app"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
