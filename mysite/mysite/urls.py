from django.contrib import admin
from django.urls import path, include
from mysite.views import start
from django.conf import settings
from django.conf.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', start),
    path('api/', include('api.urls')),
    path('', include('blog.urls')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

