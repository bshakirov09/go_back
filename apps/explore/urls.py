# Django
from django.urls import path, include
# Rest
from rest_framework.routers import DefaultRouter
# Project
from explore.views.explore import ExploreViewSet, TagViewSet

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('exp', ExploreViewSet, basename='exp')

urlpatterns = [
    path('', include(router.urls))
]
