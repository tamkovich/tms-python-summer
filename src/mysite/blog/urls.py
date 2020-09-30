from django.urls import path, re_path

from blog.views import (
    UserListView,
    UserDetailView,
    ArticleDetailView,
)


urlpatterns = [
    path('', UserListView.as_view(), name='list-users'),
    path('users/<username>/', UserDetailView.as_view(), name='get-user'),
    re_path(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view()),
]

"""
/article/bla-bla/

/users/test/
/users/admin/
/users/petia/
/users/zeka/
/users/test1245/
"""