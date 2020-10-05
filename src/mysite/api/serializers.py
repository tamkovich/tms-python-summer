from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = 'id', 'title', 'author', 'url', 'description'


'''
{
    "id": 1,
    "title": "Football",
    "author": {
        "last_name": ...,
        "first_name": ...,
    },
    "url": "http://localhost:8000/api/articles/1/"
}
'''