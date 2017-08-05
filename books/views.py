# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from books.serializers import BookSerializer
from books.models import Book

# Create your views here.

class BooksList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
