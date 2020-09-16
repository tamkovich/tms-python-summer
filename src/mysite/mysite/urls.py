from django.contrib import admin
from django.urls import path, include

from mysite.views import hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', include('blog.urls')),
]
