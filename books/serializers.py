from rest_framework import serializers
from books.models import Book,LiteraryAward

class BookSerializer(serializers.ModelSerializer):
    awards = serializers.PrimaryKeyRelatedField(many=True,queryset=LiteraryAward.objects.all(),allow_null=True,required=False)
    class Meta:
        model = Book
        fields = ('id','title','isbn','edition_language','characters','awards')
