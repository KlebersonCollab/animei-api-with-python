# Generated by Django 4.2.5 on 2023-09-07 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('status', models.CharField(choices=[('FINISHED', 'Finished'), ('IN PROGRESS', 'In Progress')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(choices=[('UHD', 'Ultra Definição'), ('HD', 'Alta Definição'), ('SD', 'Definição Padrão')], max_length=3)),
                ('url_video', models.URLField()),
                ('audio', models.CharField(choices=[('LEG', 'Legendado'), ('DUB', 'Dublado')], max_length=3)),
                ('episode', models.PositiveIntegerField()),
                ('related_anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='animei.anime')),
            ],
        ),
    ]
