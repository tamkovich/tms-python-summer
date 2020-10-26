from django.contrib.auth.models import User
from rest_framework import serializers
from profiles.models import Profile
from blog.models import Article, Category, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = 'id', 'title', 'author', 'description', 'category', 'url'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = 'text', 'author', 'article', 'created', 'active',

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'last_name', 'first_name', 'email'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = 'user', 'user_profile', 'created', 'avatar', 'info',




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
