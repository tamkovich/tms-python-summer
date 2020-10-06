from django.urls import path, re_path
from blog.views import UserListView, \
                       UserDetailView, \
                       ArticleDetailView, \
                       ArticleListView

urlpatterns = [
    path('users/<username>/', UserDetailView.as_view(), name='get-user'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('', UserListView.as_view(), name='home'),
    path('articles/<pk>/', ArticleDetailView.as_view(), name='get-article'),
]
