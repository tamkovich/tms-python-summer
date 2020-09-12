from django.conf.urls import url
from django.urls import path, include

from .views import index, book_detail, BookCreate, BookDelete, BookUpdate


urlpatterns = [
    path('', index, name='index'),
    path('index/<int:id>/', book_detail, name='book-details'),
    url(r'add_book/$', BookCreate.as_view(), name='book-add'),
    url(r'book/(?P<pk>[0-9]+)/$', BookUpdate.as_view(), name='book-update'),
    url(r'book/(?P<pk>[0-9]+)/delete/$', BookDelete.as_view(), name='book-delete'),

]
