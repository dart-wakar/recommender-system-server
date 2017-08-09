# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(blank=True, null=True)),
                ('original_title', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=300, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=300, null=True)),
                ('adult', models.BooleanField()),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('homepage', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=3, null=True)),
                ('overview', models.CharField(blank=True, max_length=500, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('release_date', models.CharField(blank=True, max_length=20, null=True)),
                ('revenue', models.BigIntegerField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('tagline', models.CharField(blank=True, max_length=60, null=True)),
                ('video', models.BooleanField()),
                ('tmdb_average_rating', models.FloatField(blank=True, null=True)),
                ('tmdb_vote_count', models.IntegerField(blank=True, null=True)),
                ('average_rating', models.FloatField()),
                ('votes_count', models.IntegerField()),
            ],
        ),
    ]
