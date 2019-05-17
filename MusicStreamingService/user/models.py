from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	id_user = models.AutoField(primary_key = True)
	surname = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	pseudo = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 254, unique = True)
	profile_pic = models.ImageField(upload_to = "img/user_avatar/")
	is_staff = models.BooleanField(default = False)

	saved_playlist = models.ManyToManyField("playlist.Playlist", related_name = "saver")
	saved_album = models.ManyToManyField("album.Album", related_name = "saved_by")
	following_artist = models.ManyToManyField("artist.Artist", related_name = "follower")
	following_user = models.ManyToManyField("self", symmetrical = False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["surname", "name", "pseudo"]

	objects = CustomUserManager()

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