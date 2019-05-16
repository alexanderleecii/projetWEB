from django.shortcuts import render
from .models import User
from playlist.models import Playlist
from album.models import Album

def display_user(request, id_user):
	if request.user.is_authenticated:
		user = User.objects.get(id_user = id_user)
		created_playlists = Playlist.objects.select_related('creator').filter(creator = id_user).order_by('update_date')[:3]
		saved_playlists = user.saved_playlist.all().order_by('update_date')[:3]
		following_count = user.following_user.all().count()

		other_users = User.objects.exclude(id_user = id_user)
		followers_count = 0
		for u in other_users:
			if u.following_user.filter(id_user = id_user).count() == 1 :
				followers_count+=1
			
		albums = user.saved_album.all().order_by('-out_date')[:3]
		return render(request, 'user/user.html', {'user' : user,
												  'following_count' : following_count,
												  'followers_count' : followers_count,
												  'created_playlists' : created_playlists,
												  'saved_playlists' : saved_playlists,
												  'albums' : albums,
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