# Generated by Django 2.2.1 on 2019-05-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190519_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pseudo',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]