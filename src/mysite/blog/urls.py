from django.urls import path, re_path

from blog.views import (
    test,
    home,
    get_user,
    create,
)


urlpatterns = [
    path('', home),
    path('users/<username>/', get_user),
    path('test/', test),
    path('create/', create),
]

"""
/users/test/
/users/admin/
/users/petia/
/users/zeka/
/users/test1245/
"""