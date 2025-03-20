# Generated by Django 5.1.7 on 2025-03-20 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_pages', '0010_remove_categoryvideo_image_categoryvideo_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyAgent',
            fields=[
                ('basecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='make_pages.basecontent')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('link_1', models.CharField(blank=True, max_length=512, null=True)),
                ('link_2', models.CharField(blank=True, max_length=512, null=True)),
                ('link_3', models.CharField(blank=True, max_length=512, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='section/%y/%m/%d/')),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
            ],
            bases=('make_pages.basecontent',),
        ),
    ]
