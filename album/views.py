from django.shortcuts import render, redirect
from album.models import Album, Song

def display_album(request, id_album):
	if request.user.is_authenticated:
		album = Album.objects.get(id_album = id_album)
		songs = Song.objects.filter(album_key = id_album)

		has_saved = (request.user.saved_album.filter(id_album = id_album).count() == 1)
		return render(request, 'album/album.html', {'Album' : album,
													'Songs' : songs,
													'has_saved' : has_saved,
											   })
	else:
		return redirect("register")