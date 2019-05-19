from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import User
from playlist.models import Playlist
from album.models import Album
from playlist.forms import PlaylistCreationForm 

def display_user(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		created_playlists = Playlist.objects.select_related('creator').filter(creator = id_user).order_by('update_date')[:3]
		saved_playlists = user.saved_playlist.all().order_by('update_date')[:3]
		following_count = user.following_user.all().count() + user.following_artist.all().count()

		other_users = User.objects.exclude(id_user = id_user)
		followers_count = 0
		for u in other_users:
			followers_count+=u.following_user.filter(id_user = id_user).count()
		
		follows = (request.user.following_user.filter(id_user = id_user).count() == 1)

		albums = user.saved_album.all().order_by('-out_date')[:3]

		if request.method == "POST":
			form = PlaylistCreationForm(request.POST, request.FILES)
			if form.is_valid():
				name = form.cleaned_data.get("playlist_name")
				description = form.cleaned_data.get("description")
				playlist_img = form.cleaned_data.get("playlist_img")

				user = User.objects.get(id_user = request.user.id_user)
				new_playlist = Playlist(name = name, description = description, playlist_img = playlist_img, creator = user)
				new_playlist.save()
				return redirect("/playlist/" + str(new_playlist.id_playlist) + "/")
		else:
			form = PlaylistCreationForm()

		return render(request, 'user/user.html', {'user' : user,
												  'following_count' : following_count,
												  'followers_count' : followers_count,
												  'follows' : follows,
												  'created_playlists' : created_playlists,
												  'saved_playlists' : saved_playlists,
												  'albums' : albums,
												  'form' : form,
												 })
	else:
		return redirect("login")

def display_created_playlists(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		created_playlists = Playlist.objects.select_related('creator').filter(creator = id_user).order_by('update_date')

		return render(request, 'user/created_playlists.html', {'user' : user,
															   'playlists' : created_playlists,
															  })
	else:
		return redirect("login")

def display_saved_playlists(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		saved_playlists = user.saved_playlist.all().order_by('update_date')

		return render(request, 'user/saved_playlists.html', {'user' : user,
															   'playlists' : saved_playlists,
															  })
	else:
		return redirect("login")

def display_saved_albums(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		saved_albums = user.saved_album.all().order_by('title')

		return render(request, 'user/saved_albums.html', {'user' : user,
														  'albums' : saved_albums,
														 })
	else:
		return redirect("login")

def display_following(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		following_users = user.following_user.all().order_by('pseudo')
		artists = user.following_artist.all().order_by('name')

		return render(request, 'user/following.html', {'user' : user,
													   'following_users' : following_users,
													   'artists' : artists,
													  })
	else:
		return redirect("login")

def display_followers(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		other_users = User.objects.exclude(id_user = id_user)

		followers = []
		for u in other_users:
			if u.following_user.filter(id_user = id_user).count() == 1 :
				followers.append({'pseudo' : u.pseudo,
								  'id_user' : u.id_user,
								  'profile_pic' : u.profile_pic
								})
		return render(request, 'user/followers.html', {'user' : user,
													   'followers' : followers,
													  })
	else:
		return redirect("login")

def save_playlist_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_playlist = request.POST.get("id_playlist")
		user.saved_playlist.add(id_playlist)
		user.save()
	return HttpResponse(request)

def unsave_playlist_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_playlist = request.POST.get("id_playlist")
		playlist = Playlist.objects.get(id_playlist = id_playlist)
		user.saved_playlist.remove(playlist)
		user.save()
	return HttpResponse(request)

def save_album_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_album = request.POST.get("id_album")
		user.saved_album.add(id_album)
		user.save()
	return HttpResponse(request)

def unsave_album_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_album = request.POST.get("id_album")
		album = Album.objects.get(id_album = id_album)
		user.saved_album.remove(album)
		user.save()
	return HttpResponse(request)

def follow_user_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_user_follow = request.POST.get("id_user")
		user.following_user.add(id_user_follow)
		user.save()
	return HttpResponse(request)

def unfollow_user_ajax(request):
	if request.is_ajax() and request.method == "POST" :
		user = request.user
		id_user_unfollow = request.POST.get("id_user_unfollow")
		user_to_unfollow = User.objects.get(id_user = id_user_unfollow)
		user.following_user.remove(user_to_unfollow)
		user.save()
	return HttpResponse(request)