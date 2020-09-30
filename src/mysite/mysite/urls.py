from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

from mysite.views import hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', include('blog.urls')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
