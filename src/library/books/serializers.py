from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Books


# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['url', 'id', 'title', 'author_name', 'description']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
