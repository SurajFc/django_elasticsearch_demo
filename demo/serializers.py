from rest_framework import serializers
from .models import Artist, Movie


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Movie
        fields = "__all__"
