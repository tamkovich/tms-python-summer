from django.urls import path,  include

from rest_framework.routers import DefaultRouter

from api.views import  ArticleViewSet
from api.views import  BookViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet)

urlpatterns = [path("", include(router.urls))]



router.register(r"books", BookViewSet)
urlpatterns = [path("", include(router.urls))]