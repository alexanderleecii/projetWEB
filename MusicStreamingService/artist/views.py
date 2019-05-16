from django.shortcuts import render, redirect

def display_artist(request, id_artist):
	if request.user.is_authenticated:
		return render(request, 'artist/artist.html', {'id_artist' : id_artist})
	else:
		return redirect("login")