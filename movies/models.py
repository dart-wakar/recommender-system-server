# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from books.models import Book

# Create your models here.

class ProductionCountry(models.Model):
    iso_3166_1 = models.CharField(max_length=3,blank=True,null=True)
    name = models.CharField(max_length=30)

class MoviesCollection(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    poster_path = models.CharField(max_length=300,blank=True,null=True)
    backdrop_path = models.CharField(max_length=300,blank=True,null=True)

class MovieGenre(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)

class ProductionCompany(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)

class SpokenLanguage(models.Model):
    iso_639_1 = models.CharField(max_length=3,blank=True,null=True)
    name = models.CharField(max_length=30)

class Keyword(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=15,blank=True,null=True)

class Movie(models.Model):
    tmdb_id = models.IntegerField(blank=True,null=True)
    imdb_id = models.CharField(max_length=10,blank=True,null=True)
    original_title = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    poster_path = models.CharField(max_length=300,blank=True,null=True)
    backdrop_path = models.CharField(max_length=300,blank=True,null=True)
    adult = models.BooleanField()
    budget = models.IntegerField(blank=True,null=True)
    homepage = models.CharField(max_length=100,blank=True,null=True)
    original_language = models.CharField(max_length=3,blank=True,null=True)
    overview = models.CharField(max_length=500,blank=True,null=True)
    popularity = models.FloatField(blank=True,null=True)
    release_date = models.CharField(max_length=20,blank=True,null=True)
    revenue = models.BigIntegerField(blank=True,null=True)
    runtime = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=20,blank=True,null=True)
    tagline = models.CharField(max_length=60,blank=True,null=True)
    video = models.BooleanField()
    tmdb_average_rating = models.FloatField(blank=True,null=True)
    tmdb_vote_count = models.IntegerField(blank=True,null=True)
    average_rating = models.FloatField(default=0.0)
    votes_count = models.IntegerField(default=0)
    production_countries = models.ManyToManyField(ProductionCountry)
    belongs_to_collection = models.ForeignKey(MoviesCollection,related_name='collection',null=True,on_delete=models.SET_NULL)
    production_companies = models.ManyToManyField(ProductionCompany)
    spoken_languages = models.ManyToManyField(SpokenLanguage)
    genres_related = models.ManyToManyField(MovieGenre)
    keywords = models.ManyToManyField(Keyword)

class VotedMovieGenre(models.Model):
    genre = models.ForeignKey(MovieGenre,related_name='genre')
    votes = models.IntegerField(blank=True,default=0)
    movie = models.ForeignKey(Movie,related_name='genres_info',null=True,on_delete=models.SET_NULL)

class VotedKeyword(models.Model):
    keyword = models.ForeignKey(Keyword,related_name='keyword')
    votes = models.IntegerField(blank=True,default=0)
    movie = models.ForeignKey(Movie,related_name='keywords_info',null=True,on_delete=models.SET_NULL)

class SimilarMovie(models.Model):
    similar_movie = models.ForeignKey(Movie,related_name='similar_movie',null=True,on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie,related_name='similar_movies_info',null=True,on_delete=models.SET_NULL)
    similarity_index = models.FloatField()

    class Meta:
        ordering = ['-similarity_index',]

class RecommendedMovie(models.Model):
    movie = models.ForeignKey(Movie,related_name='recommended_movies_info',null=True,on_delete=models.SET_NULL)
    recommended_movie = models.ForeignKey(Movie,related_name='recommended_movie',null=True,on_delete=models.SET_NULL)
    recommendation_index = models.FloatField()

    class Meta:
        ordering = ['-recommendation_index',]
