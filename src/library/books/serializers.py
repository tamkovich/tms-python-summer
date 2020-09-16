from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Books


# Serializers define the API representation.
class BookSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'groups']
