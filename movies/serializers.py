from rest_framework import serializers
from movies.models import Movie,MoviesCollection,ProductionCountry,ProductionCompany,SpokenLanguage,MovieGenre,Keyword,VotedMovieGenre,VotedKeyword,SimilarMovie,RecommendedMovie,SimilarBook,RecommendedBook
from books.models import Book
from books.serializers import BookCompactSerializer

class MoviesCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesCollection
        fields = ('id','tmdb_id','name','poster_path','backdrop_path')

class ProductionCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCountry
        fields = ('id','iso_3166_1','name')

class ProductionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCompany
        fields = ('id','tmdb_id','name')

class SpokenLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpokenLanguage
        fields = ('id','iso_639_1','name')

class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ('id','tmdb_id','name')

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id','tmdb_id','name')

class VotedMovieGenreSerializer(serializers.ModelSerializer):
    genre = MovieGenreSerializer()
    class Meta:
        model = VotedMovieGenre
        fields = ('id','genre','votes','movie')

class VotedKeywordSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer()
    class Meta:
        model = VotedKeyword
        fields = ('id','keyword','votes','movie')

class MovieCompactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','original_title','poster_path','backdrop_path')

class SimilarMovieSerializer(serializers.ModelSerializer):
    similar_movie = MovieCompactSerializer()
    class Meta:
        model = SimilarMovie
        fields = ('id','similar_movie','similarity_index','movie')

class RecommendedMovieSerializer(serializers.ModelSerializer):
    recommended_movie = MovieCompactSerializer()
    class Meta:
        model = RecommendedMovie
        fields = ('id','recommended_movie','recommendation_index','movie')

class SimilarBookSerializer(serializers.ModelSerializer):
    similar_book = BookCompactSerializer()
    class Meta:
        model = SimilarBook
        fields = ('id','similar_book','similarity_index','movie')

class RecommendedBookSerializer(serializers.ModelSerializer):
    recommended_book = BookCompactSerializer()
    class Meta:
        model = RecommendedBook
        fields = ('id','recommended_book','recommendation_index','movie')

class MovieSerializer(serializers.ModelSerializer):
    belongs_to_collection = MoviesCollectionSerializer()
    production_countries = ProductionCountrySerializer(many=True,read_only=True)
    production_companies = ProductionCompanySerializer(many=True,read_only=True)
    spoken_languages = SpokenLanguageSerializer(many=True,read_only=True)
    genres_related = MovieGenreSerializer(many=True,read_only=True)
    keywords = KeywordSerializer(many=True,read_only=True)
    genres_info = VotedMovieGenreSerializer(many=True,allow_null=True,required=False)
    keywords_info = VotedKeywordSerializer(many=True,allow_null=True,required=False)
    similar_movies_info = SimilarMovieSerializer(many=True,allow_null=True,required=False)
    recommended_movies_info = RecommendedMovieSerializer(many=True,allow_null=True,required=False)
    class Meta:
        model = Movie
        fields = ('id','tmdb_id','original_title','title','poster_path','backdrop_path','adult','budget','homepage','original_language','overview','popularity','release_date','revenue','runtime','status','tagline','video','tmdb_average_rating','tmdb_vote_count','average_rating','votes_count','belongs_to_collection','production_countries','production_companies','spoken_languages','genres_related','keywords','genres_info','keywords_info','similar_movies_info','recommended_movies_info')
