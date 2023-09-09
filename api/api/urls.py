from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from animei.views import AnimeDetail, AnimeList,EpisodeList,EpisodeDetail

schema_view = get_schema_view(
    openapi.Info(
        title="Animei API",
        default_version='v1',
        description="API para utilização do CRM de animes",
        #terms_of_service="https://www.romerosolutions.com/terms/",
        contact=openapi.Contact(email="klebersondsromero@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/animes/', AnimeList.as_view()),
    path('api/v1/animes/<int:pk>/', AnimeDetail.as_view()),

    path('api/v1/episodes/', EpisodeList.as_view()), 
    path('api/v1/episodes/<int:pk>/', EpisodeDetail.as_view()),  
    
    path('api/v1/animes/<int:pk>/episodes/', EpisodeList.as_view()),
    path('api/v1/animes/<int:pk>/episodes/<int:episode>/', EpisodeDetail.as_view()),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]