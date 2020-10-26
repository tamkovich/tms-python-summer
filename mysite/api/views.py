from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from api.serializers import ArticleSerializer, CommentSerializer, ProfileSerializer
from api.permissions import IsAuthorOrReadOnly
from blog.models import Article, Comment
from profiles.models import Profile


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = permissions.IsAuthenticated, IsAuthorOrReadOnly
    """ 
    для того чтобы только зарегестрированный пользователь мог заходить
    """
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
"""
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework import status

from blog.models import Article


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class ArticleList(APIView):
"""


#     List all snippets, or create a new snippet.

#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
