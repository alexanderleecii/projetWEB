# Generated by Django 2.2.1 on 2019-05-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190519_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='media/img/user_avatar/default_profile.png', upload_to='media/img/user_avatar/'),
        ),
    ]
