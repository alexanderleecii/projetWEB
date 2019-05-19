from django import forms

class PlaylistCreationForm(forms.Form):
	playlist_name = forms.CharField(max_length = 100,label = "Nom de la playlist :")
	description = forms.CharField(max_length = 200, label = "Description :", required = False)
	playlist_img = forms.ImageField(required = False)