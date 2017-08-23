import json
import os
import django

script_path = os.path.dirname(__file__)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommender_system_server.settings'
django.setup()

from movies.models import *

with open('data/popular_movies_recommendations.json') as data_file:
    data = json.load(data_file)

print len(data)

for i in range(0,len(data)):
    movie = Movie.objects.get(tmdb_id=data[i]['id'])
    r_ind = 0.98
    for recommended_movie_id in data[i]['recommendations']:
        try:
            recommended_movie = Movie.objects.get(tmdb_id=recommended_movie_id)
        except Movie.DoesNotExist:
            continue
        db_recommended_movie_info,recommended_movies_info_created = RecommendedMovie.objects.get_or_create(movie=movie,recommended_movie=recommended_movie,recommendation_index=r_ind)
        r_ind -= 0.02

print Movie.objects.count()
print RecommendedMovie.objects.count()
