from rest_framework.viewsets import ModelViewSet
from my_example_app.models import Musician, Album
from my_example_app.serializers import MusicianSerializer, AlbumSerializer


class MusicianViewSet(ModelViewSet):
    """
    ModelViewSet for Musician model
    """

    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class AlbumViewSet(ModelViewSet):
    """
    ModelViewSet for Album model
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
