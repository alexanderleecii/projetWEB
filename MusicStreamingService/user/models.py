from django.db import models

# Create your models here.
class User(models.Model):
	id_user = models.AutoField(primary_key = True)
	surname = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	pseudo = models.CharField(max_length = 50)
	mail = models.EmailField(max_length = 254)
	password = models.CharField(max_length = 50)
	profile_pic = models.ImageField(upload_to = "img/user_avatar/")

	saved_playlist = models.ManyToManyField("playlist.Playlist", related_name = "savers")
	saved_album = models.ManyToManyField("album.Album", related_name = "saved_by")
	following_artist = models.ManyToManyField("artist.Artist", related_name = "followers")
	following_user = models.ManyToManyField("self", symmetrical = False)

	class Meta:
		verbose_name = "user"
		ordering = ['id_user']

	def __str__(self):
		return self.pseudo

class Listening_session(models.Model):
	fk_user = models.ForeignKey("user.User", on_delete = models.PROTECT, default = 1)
	fk_song = models.ForeignKey("album.Song", on_delete = models.PROTECT, default = 1)
	date = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name = "listening"
		ordering = ['date']

	def __str__(self):
		return self.date