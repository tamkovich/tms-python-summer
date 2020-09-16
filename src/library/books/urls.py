from django.conf.urls import url
from django.urls import path

from .views import BookCreate, BookDelete, BookUpdate, BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    url(r'book_detail/(?P<pk>[0-9]+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'add_book/$', BookCreate.as_view(), name='book-add'),
    url(r'book/(?P<pk>[0-9]+)/$', BookUpdate.as_view(), name='book-update'),
    url(r'book/(?P<pk>[0-9]+)/delete/$', BookDelete.as_view(), name='book-delete'),
]
