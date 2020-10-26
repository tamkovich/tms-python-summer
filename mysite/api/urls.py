from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import ArticleViewSet, CommentViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"profiles", ProfileViewSet)

urlpatterns = [path("", include(router.urls))]
"""
from api.views import (
    ArticleList,
    ArticleDetail
)

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='list-article'),
    path('articles/<pk>/', ArticleDetail.as_view(), name='articles/<pk>'),
]

"""
"Class 'Based View'"
"""
"""
