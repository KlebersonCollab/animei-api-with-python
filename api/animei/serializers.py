from rest_framework import serializers
from .models import Anime, Episode

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'  # Você pode especificar campos específicos se desejar

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'  # Você pode especificar campos específicos se desejar
