# Generated by Django 5.1.7 on 2025-04-03 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_pages', '0014_startproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('basecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='make_pages.basecontent')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gmail', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/%y/%m/%d/')),
                ('message', models.TextField(blank=True, null=True)),
            ],
            bases=('make_pages.basecontent',),
        ),
    ]
