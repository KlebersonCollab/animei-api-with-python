
from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAdminUserOrReadOnly,IsUser

from .models import Anime, Episode
from .serializers import AnimeSerializer, EpisodeSerializer

class AnimeList(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsAdminUserOrReadOnly,IsUser]
    pagination_class = LimitOffsetPagination 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AnimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class EpisodeList(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAdminUserOrReadOnly,IsUser]
    pagination_class = LimitOffsetPagination
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)