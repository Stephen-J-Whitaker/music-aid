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
        """
        Ensure a user can't have duplciate titles
        """
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'],
                                    name='unique_user_song_title')
        ]

    def __str__(self):
        """
        Override __str__ with the correct song title
        """
        return self.title

    def get_absolute_url(self):
        """
        Provide a default success url reverse lookup
        for generic views
        """
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

    class Meta:
        """
        Ensure a user can't have duplciate setlist names
        """
        constraints = [
            models.UniqueConstraint(fields=['user', 'setlist_name'],
                                    name='unique_user_setlist_name')
        ]

    def __str__(self):
        """
        Override __str__ with the correct setlist name
        """
        return self.setlist_name
