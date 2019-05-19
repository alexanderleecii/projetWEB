# Generated by Django 2.2 on 2019-05-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id_artist', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='img/artist_photo/')),
            ],
            options={
                'verbose_name': 'artist',
                'ordering': ['id_artist'],
            },
        ),
    ]