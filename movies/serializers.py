from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','tmdb_id','original_title','title','poster_path','backdrop_path','adult','budget','homepage','original_language','overview','popularity','release_date','revenue','runtime','status','tagline','video','tmdb_average_rating','tmdb_vote_count','average_rating','votes_count')