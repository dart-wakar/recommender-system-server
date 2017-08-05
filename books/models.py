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

class Place(models.Model):
    name = models.CharField(max_length=20)

class Subject(models.Model):
    subject_type = models.CharField(max_length=15)
    subject_ol_url = models.CharField(max_length=300)
    subject_name = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600,blank=True,null=True)
    original_title = models.CharField(max_length=100)
    book_format = models.CharField(max_length=30)
    goodreads_book_id = models.IntegerField(blank=True,null=True)
    goodreads_rating = models.DecimalField(max_digits=3,decimal_places=2,null=True,blank=True)
    number_of_goodreads_rating = models.IntegerField(null=True,blank=True)
    goodreads_score = models.IntegerField(null=True,blank=True)
    isbn = models.BigIntegerField(unique=True)
    number_of_pages = models.IntegerField(null=True,blank=True)
    publish_date = models.CharField(null=True,blank=True,max_length=15)
    publishing_company = models.CharField(null=True,blank=True,max_length=30)
    ol_url = models.CharField(max_length=300,blank=True,null=True)
    ol_title = models.CharField(max_length=100,blank=True,null=True)
    ol_subtitle = models.CharField(max_length=100,blank=True,null=True)
    ol_id = models.CharField(max_length=15,unique=True)
    cover_url_small = models.CharField(max_length=150)
    cover_url_medium = models.CharField(max_length=150)
    cover_url_large = models.CharField(max_length=150)
    weight = models.CharField(max_length=50)
    edition_language = models.CharField(max_length=15,null=True,blank=True)
    characters = models.ManyToManyField(Character)
    book_series = models.ForeignKey(BookSeries,related_name='series',null=True,on_delete=models.SET_NULL)
    part_in_series = models.IntegerField(null=True,blank=True)
    author = models.ForeignKey(Author,related_name='author',null=True,on_delete=models.SET_NULL)
    places = models.ManyToManyField(Place)
    subjects = models.ManyToManyField(Subject)

    class Meta:
        ordering = ('id',)

class Excerpt(models.Model):
    text = models.CharField(max_length=300)
    comment = models.CharField(max_length=300,null=True,blank=True)
    first_sentence = models.BooleanField()
    book = models.ForeignKey(Book,related_name='excerpts',null=True,on_delete=models.SET_NULL)

class VotedGenre(models.Model):
    genre = models.ForeignKey(Genre,related_name='genre')
    votes = models.IntegerField(blank=True,default=0)
    book = models.ForeignKey(Book,related_name='genres_info',null=True,on_delete=models.SET_NULL)

class LiteraryAward(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    book = models.ForeignKey(Book,related_name='awards',null=True,on_delete=models.SET_NULL)
