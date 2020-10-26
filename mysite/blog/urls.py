from django.urls import path, re_path

from blog import forms
from blog.views import UserListView,\
                       UserDetailView,\
                       ArticleDetailView,\
                       ArticleListView,\
                       ProfileListView, ArticleDelete, \
                       UserDelete


urlpatterns = [
    path('', UserListView.as_view(), name='home'),
    path('users/', ProfileListView.as_view(), name='users'),
    path('users/<username>/', UserDetailView.as_view(), name='get-user'),
    path('users/edit/<pk>/', forms.UserForm.user_update, name='user_edit'),
    path('users/delete/<pk>/', UserDelete.as_view(), name='user_delete'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<pk>/', ArticleDetailView.as_view(), name='get-article'),
    path('new_article/', forms.ArticleForm.article_create, name='article_new'),
    path('articles/edit/<pk>/', forms.ArticleForm.article_update, name='article_edit'),
    path('articles/delete/<pk>/', ArticleDelete.as_view(), name='article_delete'),
    path('new_profile/', forms.ProfileForm.profile_create, name='profile_create'),
    path('profile/edit/<pk>/', forms.ProfileForm.profile_update, name='profile_edit'),

]
