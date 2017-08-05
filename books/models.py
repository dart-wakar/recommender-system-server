# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=30)

class BookSeries(models.Model):
    title = models.CharField(max_length=50)

class Author(models.Model):
    name = models.CharField(max_length=50)

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.BigIntegerField(unique=True)
    edition_language = models.CharField(max_length=15,null=True,blank=True)
    characters = models.ManyToManyField(Character)
    book_series = models.ForeignKey(BookSeries,related_name='series',null=True,on_delete=models.SET_NULL)
    part_in_series = models.IntegerField(null=True,blank=True)
    author = models.ForeignKey(Author,related_name='author',null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ('id',)

class VotedGenre(models.Model):
    genre = models.ForeignKey(Genre,related_name='genre')
    votes = models.IntegerField(blank=True,default=0)
    book = models.ForeignKey(Book,related_name='genres_info',null=True,on_delete=models.SET_NULL)

class LiteraryAward(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    book = models.ForeignKey(Book,related_name='awards',null=True,on_delete=models.SET_NULL)
