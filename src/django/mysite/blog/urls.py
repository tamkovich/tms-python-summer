from django.urls import path
from blog import views
from django.contrib import admin

from django.conf.urls import static
from django.conf import settings
from django.conf.urls import url
from profiles.views import get_profiles
from blog.views import test, index,goto, way, func, home, DangerDetailView, arcti,  FilmDetailView,\
    film_maker, UserListView, UserDetailView, ArticleDetailView, link_to, get_user, UserDeleteView

urlpatterns = [
    path('test/', test),
    path('func/', way),
    path('', home, name='home'),
    path('users/<username>/', UserDetailView.as_view(), name='get-user'),
    path('movie/<name>/', FilmDetailView.as_view()),
    path('main/', film_maker),
    path('class/', UserListView.as_view()),
    path('article/<pk>/', ArticleDetailView.as_view()),
    path('danger/<pk>/', DangerDetailView.as_view()),
    path('all/', arcti, name='ar'),
    path('ad/', admin.site.urls),
    path('members/', index),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    path('profiles/', get_profiles),
    path('admin/auth/user/add/', goto, name='crete-new-user'),
    path('admin/auth/user/<pk>/change/', UserDetailView.as_view(), name='update_user'),
    path('article/<pk>/delete', UserDeleteView.as_view(), name='delete_user')





] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


