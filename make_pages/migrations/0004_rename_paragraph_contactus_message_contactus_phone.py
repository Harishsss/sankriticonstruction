# Generated by Django 5.1.7 on 2025-03-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_pages', '0003_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='paragraph',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contactus',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
