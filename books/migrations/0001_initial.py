# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('original_title', models.CharField(max_length=100)),
                ('book_format', models.CharField(max_length=30)),
                ('goodreads_book_id', models.IntegerField(blank=True, null=True)),
                ('goodreads_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('number_of_goodreads_rating', models.IntegerField(blank=True, null=True)),
                ('goodreads_score', models.IntegerField(blank=True, null=True)),
                ('isbn', models.BigIntegerField(unique=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('publish_date', models.CharField(blank=True, max_length=15, null=True)),
                ('publishing_company', models.CharField(blank=True, max_length=30, null=True)),
                ('ol_url', models.CharField(blank=True, max_length=300, null=True)),
                ('ol_title', models.CharField(blank=True, max_length=100, null=True)),
                ('ol_subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('ol_id', models.CharField(max_length=15, unique=True)),
                ('cover_url_small', models.CharField(max_length=150)),
                ('cover_url_medium', models.CharField(max_length=150)),
                ('cover_url_large', models.CharField(max_length=150)),
                ('weight', models.CharField(max_length=50)),
                ('edition_language', models.CharField(blank=True, max_length=15, null=True)),
                ('part_in_series', models.IntegerField(blank=True, null=True)),
                ('average_rating', models.FloatField()),
                ('votes_count', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='books.Author')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='BookSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Excerpt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('comment', models.CharField(blank=True, max_length=300, null=True)),
                ('first_sentence', models.BooleanField()),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='excerpts', to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LiteraryAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='awards', to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_type', models.CharField(max_length=15)),
                ('subject_ol_url', models.CharField(max_length=300)),
                ('subject_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VotedGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(blank=True, default=0)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genres_info', to='books.Book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='books.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='series', to='books.BookSeries'),
        ),
        migrations.AddField(
            model_name='book',
            name='characters',
            field=models.ManyToManyField(to='books.Character'),
        ),
        migrations.AddField(
            model_name='book',
            name='places',
            field=models.ManyToManyField(to='books.Place'),
        ),
        migrations.AddField(
            model_name='book',
            name='subjects',
            field=models.ManyToManyField(to='books.Subject'),
        ),
    ]
