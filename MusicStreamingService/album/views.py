from django.shortcuts import render
from album.models import Album, Song

def display_album(request, id_album):
	return render(request, 'album/album.html', {'Album' : Album.objects.get(id_album = id_album),
												'Songs' : Song.objects.filter(album_key = id_album),
											   })