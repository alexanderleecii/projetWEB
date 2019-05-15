# Generated by Django 2.2 on 2019-05-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listening_session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'listening',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('pseudo', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='img/user_avatar/')),
            ],
            options={
                'verbose_name': 'user',
                'ordering': ['id_user'],
            },
        ),
    ]