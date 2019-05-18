from django.shortcuts import render, redirect
from MusicStreamingService.settings import STATIC_URL
from django.http import HttpResponse, JsonResponse
from playlist.models import Playlist, Song_is_in
from album.models import Album,Song
from user.models import User

def display_playlist(request, id_playlist):
	if request.user.is_authenticated:
		playlist = Playlist.objects.get(id_playlist = id_playlist)
		has_saved = (request.user.saved_playlist.filter(id_playlist = id_playlist).count() == 1)
		
		songs_query = Song_is_in.objects.select_related('id_song').filter(id_playlist = id_playlist)
		songs = []
		for song in songs_query:
			songs.append({
				'id_song' : song.id_song.id_song,
				'song_title' : song.id_song.title,
				'song_duration' : song.id_song.duration,
				'add_date' : song.add_date,
				'artist_name' : song.id_song.album_key.main_artist.name,
				'album_title' : song.id_song.album_key.title
			})

		return render(request, 'playlist/playlist.html', {'Playlist' : playlist,
														  'Songs' : songs,
														  'has_saved' : has_saved,
														 })
	else:
		return redirect("login")

def add_song_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_playlist = request.POST.get("id_playlist")
		id_song = request.POST.get("id_song")
		playlist = Playlist.objects.get(id_playlist = id_playlist)
		song = Song.objects.get(id_song = id_song)
		try:
			catch = Song_is_in.objects.get(id_playlist = playlist, id_song = song)
		except Song_is_in.DoesNotExist:
			song_addition = Song_is_in(id_playlist = playlist, id_song = song)
			song_addition.save()
			return HttpResponse(request)
	return JsonResponse({'message' : "Ce morceau est déjà dans cette playlist"})

def remove_song_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user

		id_playlist = request.POST.get("id_playlist")
		id_song = request.POST.get("id_song")

		playlist = Playlist.objects.get(id_playlist = id_playlist)
		song = Song.objects.get(id_song = id_song)

		Song_is_in.objects.get(id_playlist = playlist, id_song = song).delete()
	
	return HttpResponse(request)

def update_playlist_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		id_playlist = request.POST.get("id_playlist")
		name = request.POST.get("name")
		description = request.POST.get("description")

		playlist = Playlist.objects.get(id_playlist = id_playlist)
		
		playlist.name = name
		playlist.description = description

		playlist.save()

	return HttpResponse(request)

def delete_playlist_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		id_playlist = request.POST.get("id_playlist")
		
		playlist = Playlist.objects.get(id_playlist = id_playlist)
		
		playlist.delete()

	return HttpResponse(request)