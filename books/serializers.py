from rest_framework import serializers
from books.models import Book,LiteraryAward,VotedGenre

class BookSerializer(serializers.ModelSerializer):
    awards = serializers.PrimaryKeyRelatedField(many=True,queryset=LiteraryAward.objects.all(),allow_null=True,required=False)
    genres_info = serializers.PrimaryKeyRelatedField(many=True,queryset=VotedGenre.objects.all(),allow_null=True,required=False)
    class Meta:
        model = Book
        fields = ('id','title','isbn','edition_language','characters','awards','book_series','part_in_series','author','genres_info')
