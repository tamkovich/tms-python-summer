from django.contrib import admin
from django.urls import path, include
from mysite.views import hello
from mysite.views import give_belarus
from mysite.views import start


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('give_belarus/', give_belarus, name='FreedomBelarus'),
    path('start/', start),
    path('', include('blog.urls'))
]

