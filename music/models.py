import os
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=50)
    path_cover = models.CharField(max_length=100, blank=True)
    class Meta:
        verbose_name_plural = 'Альбомы'
    def __str__(self):
        return  self.title
class List_track(models.Model):

    album = models.ForeignKey(Album, on_delete=True)
    title = models.CharField(max_length=50, blank=True)
    #track - путь до файла
    track = models.CharField(max_length=50, blank = True)
    class Meta():
        verbose_name_plural = 'База песен'
    def __str__(self):
        return  self.title

class Playlist(models.Model):
    owner = models.ForeignKey(User, on_delete=True)
    title = models.CharField(max_length=50)
    pl_and_lt = models.ManyToManyField(List_track)
    class Meta:
        verbose_name_plural = 'Плейлисты'
    def __str__(self):
        return self.title


