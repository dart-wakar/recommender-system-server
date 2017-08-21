import json
import os
import django

script_path = os.path.dirname(__file__)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recommender_system_server.settings'
django.setup()

from movies.models import *

with open('data/details1000.json') as data_file:
    data = json.load(data_file)

#with open('data/keywords.json') as keywords_file:
    keywords_data = json.load(keywords_file)

print len(data)
#print len(keywords_data)
for i in range(0,len(data)):

    # Movie Collection
    collection = data[i]['belongs_to_collection']
    movies_collection = None
    if collection is not None:
        print 'it belongs to a collection'
        print collection['id']
        movies_collection,collection_created = MoviesCollection.objects.get_or_create(tmdb_id=collection['id'],name=collection['name'],poster_path=collection['poster_path'],backdrop_path=collection['backdrop_path'])
        print i
        print collection_created
    else:
        print 'belongs to no collection'

    # Main Movie
    tmdb_id = data[i]['id']
    imdb_id = data[i]['imdb_id']
    original_title = data[i]['original_title']
    title = data[i]['title']
    poster_path = data[i]['poster_path']
    backdrop_path = data[i]['backdrop_path']
    adult = data[i]['adult']
    budget = data[i]['budget']
    homepage = data[i]['homepage']
    original_language = data[i]['original_language']
    overview = data[i]['overview']
    popularity = data[i]['popularity']
    release_date = data[i]['release_date']
    revenue = data[i]['revenue']
    runtime = data[i]['runtime']
    status = data[i]['status']
    tagline = data[i]['tagline']
    video = data[i]['video']
    tmdb_average_rating = data[i]['vote_average']
    tmdb_vote_count = data[i]['vote_count']
    movie,movie_created = Movie.objects.get_or_create(tmdb_id=tmdb_id,imdb_id=imdb_id,original_title=original_title,title=title,poster_path=poster_path,backdrop_path=backdrop_path,adult=adult,budget=budget,homepage=homepage,original_language=original_language,overview=overview,popularity=popularity,release_date=release_date,revenue=revenue,runtime=runtime,status=status,tagline=tagline,video=video,tmdb_average_rating=tmdb_average_rating,tmdb_vote_count=tmdb_vote_count,belongs_to_collection=movies_collection)

    # Production Countries
    if data[i]['production_countries'] is not None:
        production_countries = data[i]['production_countries']
        for j in range(0,len(production_countries)):
            production_country = production_countries[j]
            db_production_country,country_created = ProductionCountry.objects.get_or_create(iso_3166_1=production_country['iso_3166_1'],name=production_country['name'])
            print j
            print country_created
            movie.production_countries.add(db_production_country)
        movie.save()

    # Movie Genre
    if data[i]['genres'] is not None:
        genres = data[i]['genres']
        for genre in genres:
            db_movie_genre,genre_created = MovieGenre.objects.get_or_create(tmdb_id=genre['id'],name=genre['name'])
            print genre['name']
            print genre_created
            voted_movie_genre,voted_movie_genre_created = VotedMovieGenre.objects.get_or_create(genre=db_movie_genre,movie=movie)
            movie.genres_related.add(db_movie_genre)
            movie.save()

    # Production Company
    if data[i]['production_companies'] is not None:
        production_companies = data[i]['production_companies']
        for production_company in production_companies:
            db_production_company,production_company_created = ProductionCompany.objects.get_or_create(tmdb_id=production_company['id'],name=production_company['name'])
            print production_company['name']
            print production_company_created
            movie.production_companies.add(db_production_company)
        movie.save()

    # Spoken Languages
    if data[i]['spoken_languages'] is not None:
        spoken_languages = data[i]['spoken_languages']
        for spoken_language in spoken_languages:
            db_spoken_language,spoken_language_created = SpokenLanguage.objects.get_or_create(iso_639_1=spoken_language['iso_639_1'],name=spoken_language['name'])
            print spoken_language['name']
            print spoken_language_created
            movie.spoken_languages.add(db_spoken_language)
        movie.save()

#for i in range(0,len(keywords_data)):
#    movie = Movie.objects.get(tmdb_id=keywords_data[i]['id'])
#    keywords = keywords_data[i]['keywords']
#    for keyword in keywords:
#        db_keyword,keyword_created = Keyword.objects.get_or_create(tmdb_id=keyword['id'],name=keyword['name'])
#        print keyword['name']
#        print keyword_created
#        voted_keyword,voted_keyword_created = VotedKeyword.objects.get_or_create(keyword=db_keyword,movie=movie)
#        movie.keywords.add(db_keyword)
#        movie.save()

print ProductionCountry.objects.count()
print MoviesCollection.objects.count()
print MovieGenre.objects.count()
print ProductionCompany.objects.count()
print SpokenLanguage.objects.count()
print Keyword.objects.count()
print Movie.objects.count()
