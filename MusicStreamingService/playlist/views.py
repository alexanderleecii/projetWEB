from django.shortcuts import render, redirect
from playlist.models import Playlist, Song_is_in
from album.models import Album,Song
from user.models import User

def display_playlist(request, id_playlist):
	if request.user.is_authenticated:
		playlist = Playlist.objects.get(id_playlist = id_playlist)
		
		songs_query = Song_is_in.objects.select_related('id_song').filter(id_playlist = id_playlist)
		songs = []
		for song in songs_query:
			songs.append({
				'song_title' : song.id_song.title,
				'song_duration' : song.id_song.duration,
				'add_date' : song.add_date,
				'artist_name' : song.id_song.album_key.artist_key.name,
				'album_title' : song.id_song.album_key.title
			})

		return render(request, 'playlist/playlist.html', {'Playlist' : playlist,
														  'Songs' : songs,
														 })
	else:
		return redirect("login")
