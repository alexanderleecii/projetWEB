from django.db import models

# Create your models here.
class Artist(models.Model):
	id_artist = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	photo = models.ImageField(upload_to = "img/artist_photo/")

	followed_by = models.ManyToManyField("user.User")
	appears_in = models.ManyToManyField("album.Song")
	
	class Meta:
		verbose_name = "artist"
		ordering = ['id_artist']

	def __str__(self):
		return self.name