from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Song(models.Model):
    """
    Model class to hold song and lyric details
    """
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150, blank=True)
    lyrics = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_songs")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'],
                                    name='unique_user_song_title')
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('song_edit', kwargs={'pk': self.pk})


class Setlist(models.Model):
    """
    Model class to hold setlists
    """
    setlist_name = models.CharField(max_length=150)
    songs_in_setlist = models.ManyToManyField(Song,
                                              related_name="songs_in_setlist")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="setlist_user")

    def __str__(self):
        return self.setlist_name
