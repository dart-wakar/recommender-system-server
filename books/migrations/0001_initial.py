# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 17:42
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
                ('isbn', models.BigIntegerField(unique=True)),
                ('edition_language', models.CharField(blank=True, max_length=15, null=True)),
                ('part_in_series', models.IntegerField(blank=True, null=True)),
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
    ]
