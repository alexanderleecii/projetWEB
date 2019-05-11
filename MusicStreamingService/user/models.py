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

	following_user = models.ManyToManyField("self", symmetrical = False)
	saved_playlist = models.ManyToManyField("playlist.Playlist")

	class Meta:
		verbose_name = "user"
		ordering = ['id_user']

	def __str__(self):
		return self.pseudo

class Listening_session(models.Model):
	fk_user = models.ForeignKey("User", on_delete = models.PROTECT)
	fk_song = models.ForeignKey("album.Song", on_delete = models.PROTECT)
	date = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name = "listening"
		ordering = ['date']

	def __str__(self):
		return self.date