from django.contrib import admin
from .models import Playlist, Song_is_in

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Song_is_in)