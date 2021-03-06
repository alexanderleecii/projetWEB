# Generated by Django 2.2 on 2019-05-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song_is_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'song_is_in',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id_playlist', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=254)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('playlist_img', models.ImageField(upload_to='img/playlist_cover/')),
                ('contains', models.ManyToManyField(related_name='in_playlists', to='album.Song')),
            ],
            options={
                'verbose_name': 'playlist',
                'ordering': ['update_date'],
            },
        ),
    ]
