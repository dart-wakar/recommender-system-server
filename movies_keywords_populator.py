import json
import os
import django

script_path = os.path.dirname(__file__)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommender_system_server.settings'
django.setup()

from movies.models import *

with open('data/popular_movies_keywords.json') as data_file:
    data = json.load(data_file)

print len(data)

for i in range(0,len(data)):
    movie = Movie.objects.get(tmdb_id=data[i]['id'])
    keywords = data[i]['keywords']
    for keyword in keywords:
        db_keyword,keyword_created = Keyword.objects.get_or_create(tmdb_id=keyword['id'],name=keyword['name'])
        print keyword['name']
        print keyword_created
        voted_keyword,voted_keyword_created = VotedKeyword.objects.get_or_create(keyword=db_keyword,movie=movie)
        movie.keywords.add(db_keyword)
        movie.save()

print Movie.objects.count()
print Keyword.objects.count()
print VotedKeyword.objects.count()
