from rest_framework import serializers
from movies.models import Movie,MoviesCollection,ProductionCountry,ProductionCompany,SpokenLanguage,MovieGenre,Keyword

class MoviesCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesCollection
        fields = ('id','tmdb_id','name','poster_path','backdrop_path')

class ProductionCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCountry
        fields = ('id','iso_3166_1','name')

class MovieSerializer(serializers.ModelSerializer):
    belongs_to_collection = MoviesCollectionSerializer()
    production_countries = ProductionCountrySerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = ('id','tmdb_id','original_title','title','poster_path','backdrop_path','adult','budget','homepage','original_language','overview','popularity','release_date','revenue','runtime','status','tagline','video','tmdb_average_rating','tmdb_vote_count','average_rating','votes_count','belongs_to_collection','production_countries','production_companies','spoken_languages','genres_related','keywords')
