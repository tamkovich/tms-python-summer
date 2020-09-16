from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from books.models import Books
from books.serializers import UserSerializer, BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
        return Response(data)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Books.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_paginated_response(self, data):
        return Response(data)
