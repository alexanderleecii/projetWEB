from django.template.context_processors import csrf
from django.core import serializers
from django.shortcuts import render
from playlist.models import Playlist
from album.models import Album,Song
from artist.models import Artist
from user.models import User
import json

def home(request):
	if request.user.is_authenticated:
		playlists = Playlist.objects.all()
		albums = Album.objects.all()
		songs = Song.objects.all()
		artists = Artist.objects.all()
		users = User.objects.all()

		songsjson = serializers.serialize("json", songs)
		playlistsjson = serializers.serialize("json", playlists)
		albumsjson = serializers.serialize("json", albums)
		artistsjson = serializers.serialize("json", artists)
		usersjson = serializers.serialize("json", users)

		result = {}
		result.update(csrf(request))
		result['playlists'] = playlists.order_by('update_date')[:4]
		result['albums'] = albums.order_by('out_date')[:4]
		return render(request, 'browse/index.html', {'result' : result, 
													 'songsjson' : songsjson,
													 'playlistsjson' : playlistsjson,
													 'albumsjson' : albumsjson,
													 'artistsjson' : artistsjson,
													 'usersjson' : usersjson 
													})
	else:
		return redirect("login")

def display_latest_playlists(request):

	return render(request, 'browse/latest_playlists.html')

def display_latest_albums(request):

	return render(request, 'browse/latest_albums.html')
		
