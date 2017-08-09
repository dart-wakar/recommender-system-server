# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    original_title = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    poster_path = models.CharField(max_length=300,blank=True,null=True)
    backdrop_path = models.CharField(max_length=300,blank=True,null=True)
    adult = models.BooleanField()
    budget = models.IntegerField(blank=True,null=True)
    homepage = models.CharField(blank=True,null=True)
    original_language = models.CharField(max_length=3,blank=True,null=True)
    overview = models.CharField(max_length=500,blank=True,null=True)
    popularity = models.FloatField(blank=True,null=True)
    release_date = models.CharField(max_length=20,blank=True,null=True)
    revenue = models.BigIntegerField(blank=True,null=True)
    runtime = models.IntegerField(blank=True,null=True)
    status = models.CharField(blank=True,null=True)
    tagline = models.CharField(max_length=60,blank=True,null=True)
    video = models.BooleanField()
    tmdb_average_rating = models.FloatField(blank=True,null=True)
    tmdb_vote_count = models.IntegerField(blank=True,null=True)
    average_rating = models.FloatField()
    votes_count = models.IntegerField()
