from django.contrib import admin
from django.urls import path, include
from mysite.views import start
from django.conf import settings
from django.conf.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', start),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('blog.urls')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)