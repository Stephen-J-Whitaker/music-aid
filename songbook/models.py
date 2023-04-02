from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Song(models.Model):
    """
    Model to hold song and lyric details
    """
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150, blank=True)
    lyrics = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_songs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('edit_song', kwargs={'pk': self.pk})
