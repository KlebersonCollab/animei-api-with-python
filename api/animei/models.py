from django.db import models

# Create your models here.
class Anime(models.Model):
    STATUS_CHOICE = {
        ('FINISHED', 'Finished'),
        ('IN PROGRESS', 'In Progress'),
    }
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    quality = models.CharField(max_length=3, choices=QUALITY_CHOICES)
    url_video = models.URLField()
    audio = models.CharField(max_length=3, choices=AUDIO_CHOICES)
    episode = models.PositiveIntegerField()
    related_anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episode')
    
    def __str__(self):
        return f"{self.related_anime.name} - Episódio {self.episode}"

