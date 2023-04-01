from .models import Song
from django import forms


class AddSong(forms.ModelForm):
    """
    Form for adding song data
    """
    class Meta:
        model = Song
        fields = ('title', 'artist', 'lyrics',)
