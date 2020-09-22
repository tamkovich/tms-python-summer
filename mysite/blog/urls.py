from django.urls import path, re_path
from blog.views import UserListView, \
                       UserDetailView, \
                       ArticleDetailView, \
                       ArticleListView


urlpatterns = [
    path('users/<username>/', UserDetailView.as_view()),
    # path('create/', create),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('', UserListView.as_view(), name='home'),
    path('article/<pk>/', ArticleDetailView.as_view()),
]
