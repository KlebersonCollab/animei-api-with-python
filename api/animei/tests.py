from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from .models import Anime, Episode

class AnimeEpisodeAPITest(TestCase):
    def setUp(self):
        # Criar um superusuário para testes
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        
        # Criar um grupo "admin" e adicionar o superusuário a ele
        self.admin_group = Group.objects.create(name='admin')
        self.admin_user.groups.add(self.admin_group)

        # Criar um cliente de API
        self.client = APIClient()

        # Criar alguns objetos Anime e Episode para testes
        self.anime_data = {
            "name": "Anime de Teste",
            "description": "Descrição do Anime de Teste",
            "genre": "Ação",
            "year": 2022,
            "status": "EM_ANDAMENTO"
        }
        self.anime = Anime.objects.create(**self.anime_data)
        
        self.episode_data = {
            "title": "Episódio 1",
            "description": "Descrição do Episódio 1",
            "anime": self.anime
        }
        self.episode = Episode.objects.create(**self.episode_data)
        
    def test_list_animes(self):
        # Testar a rota de listagem de animes (GET)
        response = self.client.get('/api/v1/animes/')
        self.assertEqual(response.status_code, 200)
    
    def test_retrieve_anime(self):
        # Testar a rota de detalhes do anime (GET)
        response = self.client.get(f'/api/v1/animes/{self.anime.id}/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_anime(self):
        # Testar a criação de um novo anime (POST)
        self.client.force_authenticate(user=self.admin_user)  # Autenticar como usuário admin
        response = self.client.post('/api/v1/animes/', self.anime_data, format='json')
        self.assertEqual(response.status_code, 201)
    
    def test_update_anime(self):
        # Testar a atualização de um anime existente (PUT)
        self.client.force_authenticate(user=self.admin_user)  # Autenticar como usuário admin
        updated_data = {
            "name": "Anime Atualizado",
            "description": "Descrição do Anime Atualizado",
            "genre": "Comédia",
            "year": 2023,
            "status": "FINALIZADO"
        }
        response = self.client.put(f'/api/v1/animes/{self.anime.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_anime(self):
        # Testar a exclusão de um anime existente (DELETE)
        self.client.force_authenticate(user=self.admin_user)  # Autenticar como usuário admin
        response = self.client.delete(f'/api/v1/animes/{self.anime.id}/')
        self.assertEqual(response.status_code, 204)
    
    # Testes semelhantes para as rotas de Episode
