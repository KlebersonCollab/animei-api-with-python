## API para o CRM de Animes (Projeto Animei)

Para criar uma API que se comunique com um banco de dados usando um ORM (Object-Relational Mapping) em Python com o framework Django, você pode seguir os seguintes passos:

#### Instalação do Django:

1 - Certifique-se de que você tem o Django instalado. Se não tiver, você pode instalá-lo usando o pip:

```bash
pip install Django
```

2 - Crie um novo projeto Django:
Inicie um novo projeto Django executando o seguinte comando:

```bash
django-admin startproject api
```

3 - Crie um aplicativo Django:
Dentro do seu projeto, crie um aplicativo usando o seguinte comando:
Instalação do Django

```bash
python manage.py startapp animei_api
```


4 - Defina seu modelo de dados:
Em seu aplicativo, defina os modelos de dados que representam as tabelas do seu banco de dados. Isso é feito em um arquivo chamado models.py dentro do diretório do aplicativo.

Exemplo de um modelo simples:

```python
from django.db import models

# Create your models here.
class Anime(models.Model):
    STATUS_CHOICE = {
        ('FINISHED', 'Finished'),
        ('IN PROGRESS', 'In Progress'),
    }
    name = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    year = models.IntegerField()  
    status = models.CharField(max_length=12,choices=STATUS_CHOICE)

    def __str__(self):
        return self.name

class Episode(models.Model):
    
    QUALITY_CHOICES = (
        ('UHD', 'Ultra Definição'),
        ('HD', 'Alta Definição'),
        ('SD', 'Definição Padrão'),
    )
    AUDIO_CHOICES=(
        ('LEG', 'Legendado'),
        ('DUB', 'Dublado'),
    )

    quality = models.CharField(max_length=3, choices=QUALITY_CHOICES)
    url_video = models.URLField()
    audio = models.CharField(max_length=3, choices=AUDIO_CHOICES)
    episode = models.PositiveIntegerField()
    related_anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episode')
    
    def __str__(self):
        return f"{self.related_anime.name} - Episódio {self.episode}"
```

5 - Crie migrações e aplique-as:
Depois de definir seus modelos, você precisa criar migrações para criar as tabelas no banco de dados:

```bash
python manage.py makemigrations
```
E, em seguida, aplique as migrações:

```bash
python manage.py migrate
```
6 - Crie as views da API:
Crie views que definam como os dados serão expostos pela sua API. Você pode usar as classes de visualização genéricas do Django, como APIView ou ViewSet, para criar endpoints da API.

Instale o rest_framework

```bash
pip install djangorestframework
```
Exemplo de uma view usando APIView:

```python
from rest_framework import generics
from .models import Anime, Episode
from .serializers import AnimeSerializer, EpisodeSerializer

class AnimeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class AnimeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class EpisodeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
```
7 - Crie serializers:
Crie serializers para converter os objetos do modelo em formato JSON. Você pode usar o Django Rest Framework para simplificar esse processo.

Exemplo de um serializer:

```python
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Anime, Episode
from .serializers import AnimeSerializer, EpisodeSerializer

class AnimeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class AnimeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class EpisodeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

```

8 - Configure as URLs da API:
Configure as URLs para suas views da API no arquivo urls.py do seu aplicativo.

```python
from django.contrib import admin
from django.urls import path

from animei.views import AnimeListCreateAPIView,EpisodeListCreateAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/animes/', AnimeListCreateAPIView.as_view(), name='list all animes'),
    path('api/v1/episodes/', EpisodeListCreateAPIView.as_view(), name='list all episodes'),
]

```

9 - Execute o servidor de desenvolvimento:
Inicie o servidor de desenvolvimento Django para testar sua API:

```bash
python manage.py runserver
```

Agora, você deve ter uma API simples que se comunica com um banco de dados usando um ORM Django. Você pode acessar seus endpoints API em http://localhost:8000/swagger/ (ou o caminho que você configurou) para obter os dados do banco de dados. Certifique-se de instalar o Django Rest Framework se você não o tiver feito para obter funcionalidades adicionais para suas APIs.

![Swagger](https://cdn.discordapp.com/attachments/1116505268788928574/1149942757369069568/image.png)

10 - Criando seu super usuário:

```bash
python manage.py createsuperuser
```


##### OBS: *caso você use apenas como api não esqueça de adicionar no settings.py o seguinte codigo*:

```python
# return Json API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
```

11 - Gerando documentação

Para gerar uma doc openapi siga os passos:

* Instale a biblioteca drf-yasg:
    ```bash
    pip install drf-yasg
    ```
* Adicione 'drf_yasg' ao INSTALLED_APPS em seu arquivo settings.py:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'animei',
        'drf_yasg',
    ]
    ```
