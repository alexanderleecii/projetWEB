# Generated by Django 2.2 on 2019-05-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0006_auto_20190516_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='contains',
        ),
    ]
