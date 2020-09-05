from django.conf.urls import url
from django.urls import path
from .views import ProductCreate, ProductUpdate, ProductDelete, index

urlpatterns = [
    path('', index, name='index'),
    url(r'add_product/$', ProductCreate.as_view(), name='product-add'),
    url(r'product/(?P<pk>[0-9]+)/$', ProductUpdate.as_view(), name='product-update'),
    url(r'product/(?P<pk>[0-9]+)/delete/$', ProductDelete.as_view(), name='product-delete'),
]
