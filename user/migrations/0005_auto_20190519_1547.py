# Generated by Django 2.2.1 on 2019-05-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190517_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/user_avatar/'),
        ),
    ]
