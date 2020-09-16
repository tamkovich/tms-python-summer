from django.urls import path

from blog.views import test, func, home, get_user

urlpatterns = [
    path('test/', test),
    path('func/', func),
    path('', home),
    path('users/<username>/', get_user)



]
#python3 manage.py runserver