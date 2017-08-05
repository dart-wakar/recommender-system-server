# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.BigIntegerField(unique=True)
    edition_language = models.CharField(max_length=15)
    characters = models.ManyToManyField(Character)

    class Meta:
        ordering = ('id',)

class LiteraryAward(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    book = models.ForeignKey(Book,related_name='awards',null=True,on_delete=models.SET_NULL)
