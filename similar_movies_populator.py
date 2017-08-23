import json
import os
import django

script_path = os.path.dirname(__file__)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommender_system_server.settings'
django.setup()

from movies.models import *

with open('data/popular_movies_similar.json') as data_file:
    data = json.load(data_file)

print len(data)

for i in range(0,len(data)):
    movie = Movie.objects.get(tmdb_id=data[i]['id'])
    s_ind = 0.98
    for similar_movie_id in data[i]['similar']:
        try:
            similar_movie = Movie.objects.get(tmdb_id=similar_movie_id)
        except Movie.DoesNotExist:
            continue
        similar_movie = Movie.objects.get(tmdb_id=similar_movie_id)
        db_similar_movie_info,similar_movies_info_created = SimilarMovie.objects.get_or_create(movie=movie,similar_movie=similar_movie,similarity_index=s_ind)
        s_ind -= 0.02

print Movie.objects.count()
print SimilarMovie.objects.count()
