from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    """
    Model to hold song and lyric details
    """
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150, blank=True)
    lyrics = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_songs")
    song_slug = models.SlugField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
