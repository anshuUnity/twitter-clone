# Generated by Django 3.0.8 on 2021-04-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_tweet_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/audio'),
        ),
    ]
