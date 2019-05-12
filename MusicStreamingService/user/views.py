from django.shortcuts import render
from .models import User
from playlist.models import Playlist
from album.models import Album


def display_user(request, id_user):
	user = User.objects.get(id_user = id_user)
	created_playlists = Playlist.objects.select_related('creator').filter(creator = id_user).order_by('update_date')
	#saved_playlists = Playlist.objects.select_related('saved_playlists').filter(id_user = id_user).order_by('-id')
	saved_playlists = user.saved_playlist.all().order_by('-update_date')[:3]

	albums = user.saved_album.all().order_by('-out_date')[:3]
	return render(request, 'user/user.html', {'user' : user,
											  'created_playlists' : created_playlists,
											  'saved_playlists' : saved_playlists,
											  'albums' : albums,
											 })

def display_created_playlists(request, id_user):

	return render(request, 'user/created_playlists.html')