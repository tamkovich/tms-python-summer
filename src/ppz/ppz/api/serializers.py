from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import Article

from blog.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Book
        fields = 'id', 'title', 'author', 'description', 'author_id'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author  = AuthorSerializer(read_only=True)
    class Meta:  
        model =  Article
        fields = 'id', 'title', 'author', 'url', 'description', 'author_id'