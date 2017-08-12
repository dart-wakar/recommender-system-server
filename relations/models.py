# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from movies.models import Movie
from books.models import Book

# Create your models here.

class MovieMovieSimilarRelation(models.Model):
    movie_1 = models.ForeignKey(Movie,related_name='similar_movies_info',null=True,on_delete=models.SET_NULL)
    movie_2 = models.ForeignKey(Movie,related_name='similar_movies_info',null=True,on_delete=models.SET_NULL)
    similarity_index = models.FloatField()

    class Meta:
        ordering = ('-similarity_index')

class MovieMovieRecommendationRelation(models.Model):
    movie_1 = models.ForeignKey(Movie,related_name='recommended_movies_info',null=True,on_delete=models.SET_NULL)
    movie_2 = models.ForeignKey(Movie,related_name='recommended_movies_info',null=True,on_delete=models.SET_NULL)
    recommendation_index = models.FloatField()

    class Meta:
        ordering = ('-recommendation_index')

class MovieBookSimilarRelation(models.Model):
    movie = models.ForeignKey(Movie,related_name='similar_books_info',null=True,on_delete=models.SET_NULL)
    book = models.ForeignKey(Book,related_name='similar_movies_info',null=True,on_delete=models.SET_NULL)
    similarity_index = models.FloatField()

    class Meta:
        ordering = ('-similarity_index')

class MovieBookRecommendationRelation(models.Model):
    movie = models.ForeignKey(Movie,related_name='recommended_books_info',null=True,on_delete=models.SET_NULL)
    book = models.ForeignKey(Book,related_name='recommended_movies_info',null=True,on_delete=models.SET_NULL)
    recommendation_index = models.FloatField()

    class Meta:
        ordering = ('-recommendation_index')
