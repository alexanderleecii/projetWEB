from django.shortcuts import render, redirect
from album.models import Album, Song
from playlist.models import Playlist, Song_is_in
from user.models import User
from artist.models import Artist

def display_artist(request, id_artist):
	if request.user.is_authenticated:
		artist = Artist.objects.get(id_artist = id_artist)
		albums = Album.objects.filter(main_artist__pk = id_artist)
		followers_count = User.objects.filter(following_artist__pk = id_artist).count()
		song_features = Song.objects.filter(artist_featured__pk = id_artist)
		album_features = Album.objects.filter(song__in = song_features).exclude(main_artist__pk = id_artist).distinct()

		songs_query = Song_is_in.objects.filter(id_song__in = song_features.values('id_song'))
		playlists = Playlist.objects.filter(id_playlist__in = songs_query.values('id_playlist')).distinct()

		follows = (request.user.following_artist.filter(id_artist = id_artist).count() == 1)

		return render(request, 'artist/artist.html', {'artist' : artist,
													  'followers_count' : followers_count,
													  'albums' : albums,
													  'album_features' : album_features,
													  'playlists' : playlists,
													  'follows' : follows,
													 })
	else:
		return redirect("login")

def display_artist_albums(request, id_artist):
	if request.user.is_authenticated:
		artist = Artist.objects.get(id_artist = id_artist)
		albums = Album.objects.filter(main_artist__pk = id_artist)
		return render(request, 'artist/artist_albums.html', {'artist' : artist,
															 'albums' : albums,
															})
	else:
		return redirect("login")

def followers(request, id_artist):
	if request.user.is_authenticated:
		artist = Artist.objects.get(id_artist = id_artist)
		followers = User.objects.filter(following_artist__pk = id_artist)
		return render(request, 'artist/followers.html', {'artist' : artist,
														 'followers' : followers,
														})
	else:
		return redirect("login")

def artist_is_in_playlist(request, id_artist):
	if request.user.is_authenticated:
		artist = Artist.objects.get(id_artist = id_artist)
		song_features = Song.objects.filter(artist_featured__pk = id_artist)
		songs_query = Song_is_in.objects.filter(id_song__in = song_features.values('id_song'))
		playlists = Playlist.objects.filter(id_playlist__in = songs_query.values('id_playlist')).distinct()
		return render(request, 'artist/playlists.html', {'artist' : artist,
														 'playlists' : playlists,
														})
	else:
		return redirect("login")

def display_artist_albums_features(request, id_artist):
	if request.user.is_authenticated:
		artist = Artist.objects.get(id_artist = id_artist)
		albums = Album.objects.select_related('main_artist').filter(main_artist = id_artist).order_by('out_date')
		return render(request, 'artist/artist_albums_features.html', {'artist' : artist,
															 		  'albums' : albums,
																	 })
	else:
		return redirect("login")

def follow_artist_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_artist_follow = request.POST.get("id_artist")
		user.following_artist.add(id_artist_follow)
		user.save()
	return HttpResponse(request)

def unfollow_artist_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_artist_unfollow = request.POST.get("id_artist_unfollow")
		artist_to_unfollow = Artist.objects.get(id_artist = id_artist_unfollow)
		user.following_artist.remove(artist_to_unfollow)
		user.save()
	return HttpResponse(request)