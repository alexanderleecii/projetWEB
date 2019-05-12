from django.db import models

# Create your models here.
class Album(models.Model):
	id_album = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 100)
	out_date = models.DateField(auto_now_add = True)
	album_img = models.ImageField(upload_to = "img/album_cover/")

	artist_key = models.ForeignKey("artist.Artist", on_delete = models.CASCADE, default = 1)
	
	class Meta:
		verbose_name = "album"
		ordering = ['out_date']

	def __str__(self):
		return self.title

class Song(models.Model):
	id_song = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 100)
	duration = models.CharField(max_length = 5)
	out_date = models.DateField(auto_now_add = True)
	file = models.FileField(upload_to = "songs/")

	album_key = models.ForeignKey("album.Album", on_delete = models.PROTECT, default = 1)
	features = models.ManyToManyField("artist.Artist", related_name = "appears_in")

	class Meta:
		verbose_name = "song"
		ordering = ['album_key','out_date']

	def __str__(self):
		return self.title