# TripMate_app/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet, DestinationImageViewSet

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)
router.register(r'images', DestinationImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
