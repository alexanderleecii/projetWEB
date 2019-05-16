from django.shortcuts import render

def display_artist(request, id_artist):
	return render(request, 'artist/artist.html', {'id_artist' : id_artist})