from django.urls import path, include
from rest_framework.routers import DefaultRouter

from my_example_app.views import MusicianViewSet, AlbumViewSet

router = DefaultRouter()

router.register(r'musician', MusicianViewSet, basename="musician")
router.register(r'album', AlbumViewSet, basename="album")

urlpatterns = [
    path('', include(router.urls)),
]
