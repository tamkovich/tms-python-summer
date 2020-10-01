from rest_framework.viewsets import ModelViewSet


from api.serializers import BookSerializer
from api.serializers import ArticleSerializer

from blog.models import Article
from blog.models import Book


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


