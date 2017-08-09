# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    original_title = models.CharField(max_length=100,blank=True,null=True)
    poster_path = models.CharField(max_length=300,blank=True,null=True)
    backdrop_path = models.CharField(max_length=300,blank=True,null=True)
    adult = models.BooleanField()
    budget = models.IntegerField(blank=True,null=True)
    homepage = models.CharField(blank=True,null=True)
    original_language = models.CharField(max_length=3,blank=True,null=True)
    
