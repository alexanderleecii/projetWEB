from django.db import models

# Create your models here.
class Playlist(models.Model):
	id_playlist = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 254)
	creation_date = models.DateField(auto_now_add = True)
	update_date = models.DateField(auto_now = True)
	playlist_img = models.ImageField(upload_to = "img/playlist_cover/")

	creator = models.ForeignKey("user.User", on_delete = models.CASCADE)

	class Meta:
		verbose_name = "playlist"
		ordering = ['update_date']

	def __str__(self):
		return self.name

class Song_is_in(models.Model):
	id_playlist = models.ForeignKey("Playlist", on_delete = models.CASCADE)
	id_song = models.ForeignKey("album.Song", on_delete = models.CASCADE)
	add_date = models.DateField(auto_now_add = True)

	class Meta:
		verbose_name = "song_is_in"
		ordering = ['id_playlist', 'id_song']

	def __str__(self):
		return self.add_date