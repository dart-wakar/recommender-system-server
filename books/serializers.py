from rest_framework import serializers
from books.models import Book,LiteraryAward,VotedGenre,Character,Author,BookSeries,Genre

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id','name')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name')

class BookSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSeries
        fields = ('id','title')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name')

class VotedGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotedGenre
        fields = ('id','genre','votes','book')

class BookSerializer(serializers.ModelSerializer):
    awards = serializers.PrimaryKeyRelatedField(many=True,queryset=LiteraryAward.objects.all(),allow_null=True,required=False)
    genres_info = serializers.PrimaryKeyRelatedField(many=True,queryset=VotedGenre.objects.all(),allow_null=True,required=False)
    characters = CharacterSerializer(many=True,read_only=True)
    author = AuthorSerializer()
    book_series = BookSeriesSerializer()
    class Meta:
        model = Book
        fields = ('id','title','isbn','edition_language','characters','awards','book_series','part_in_series','author','genres_info')
