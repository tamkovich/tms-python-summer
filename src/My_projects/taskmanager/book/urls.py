from django.urls import path
from .views import BookListView, \
                   BookDetailView
app_name = "books"

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('book/<pk>/', BookDetailView.as_view()),
]

