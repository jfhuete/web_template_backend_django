from rest_framework import serializers
from my_example_app.models import Musician, Album


class MusicianSerializer(serializers.ModelSerializer):
    """
    Serializer for Musician Model
    """

    class Meta:
        model = Musician
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for Album Model
    """

    artist = MusicianSerializer()

    class Meta:
        model = Album
        fields = "__all__"
