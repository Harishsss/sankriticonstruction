# Generated by Django 5.1.7 on 2025-03-17 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_pages', '0009_categoryvideo_ongoingproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryvideo',
            name='image',
        ),
        migrations.AddField(
            model_name='categoryvideo',
            name='video',
            field=models.URLField(blank=True, max_length=1010, null=True),
        ),
    ]
