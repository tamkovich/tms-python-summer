from django.urls import path
from blog.views import UserListView, UserDetailView, ArticleDetailView, BookDetailView



urlpatterns = [
    path('', UserListView.as_view()),
    path('users/<username>/', UserDetailView.as_view()),
    path('article/<pk>/', ArticleDetailView.as_view()),
    path('book/<pk>/', BookDetailView.as_view()),
]