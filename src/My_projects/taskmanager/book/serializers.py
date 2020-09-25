from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    description = serializers.CharField()
    author = serializers.CharField(max_length=50)
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class BookSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    author = serializers.CharField(max_length=50)
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)