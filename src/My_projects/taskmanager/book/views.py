from django.shortcuts import get_object_or_404, render


from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer, BookSerializers

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = request.data.get('book')

        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book_saved.title)})

class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

