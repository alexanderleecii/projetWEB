from django.template.context_processors import csrf
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from playlist.models import Playlist, Song_is_in
from album.models import Album,Song
from artist.models import Artist
from user.models import User
from playlist.forms import PlaylistCreationForm
import json

def home(request):
	if request.user.is_authenticated:
		playlists = Playlist.objects.all()
		albums = Album.objects.all()
		songs = Song.objects.all()
		artists = Artist.objects.all()
		users = User.objects.all()

		created_playlists = Playlist.objects.select_related('creator').filter(creator = request.user.id_user).order_by('update_date')
		
		saved_playlists = request.user.saved_playlist.all()
		saved_albums = request.user.saved_album.all()

		songsjson = serializers.serialize("json", songs)
		playlistsjson = serializers.serialize("json", playlists)
		albumsjson = serializers.serialize("json", albums)
		artistsjson = serializers.serialize("json", artists)
		usersjson = serializers.serialize("json", users)

		saved_playlists_json = serializers.serialize("json", saved_playlists)
		saved_albums_json = serializers.serialize("json", saved_albums)

		result = {}
		result.update(csrf(request))
		result['playlists'] = playlists.order_by('-update_date')[:4]
		result['albums'] = albums.order_by('-out_date')[:4]

		form = PlaylistCreationForm()

		return render(request, 'browse/index.html', {'result' : result,
													 'created_playlists' : created_playlists,
													 'songsjson' : songsjson,
													 'playlistsjson' : playlistsjson,
													 'albumsjson' : albumsjson,
													 'artistsjson' : artistsjson,
													 'usersjson' : usersjson,
													 'saved_playlists_json' : saved_playlists_json,
													 'saved_albums_json' : saved_albums_json,
													 'form' : form,
													})
	else:
		return redirect("login")

def display_latest_playlists(request):
	if request.user.is_authenticated:
		return render(request, 'browse/latest_playlists.html')
	else:
		return redirect("login")

def display_latest_albums(request):
	if request.user.is_authenticated:
		return render(request, 'browse/latest_albums.html')
	else:
		return redirect("login")