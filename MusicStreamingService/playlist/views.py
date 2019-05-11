from django.shortcuts import render
from playlist.models import Playlist, Song_is_in
from album.models import Album,Song

# Create your views here.
def display_playlist(request, id_playlist):

	return render(request, 'playlist/playlist.html', {'Playlist' : Playlist.objects.get(id_playlist = id_playlist),
													  'Songs' : zip(Song.objects.filter(id_song__in = 
													  	Song_is_in.objects.filter(id_playlist = id_playlist).values_list('id_song')),
													  	Song_is_in.objects.filter(id_playlist = id_playlist).values_list('add_date', flat=True))
													 })

	