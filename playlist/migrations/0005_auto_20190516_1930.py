# Generated by Django 2.2 on 2019-05-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_auto_20190516_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='playlist_img',
            field=models.ImageField(blank=True, null=True, upload_to='img/playlist_cover/'),
        ),
    ]
