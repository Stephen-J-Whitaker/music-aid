from django import forms
from .models import Song


class AddSong(forms.ModelForm):
    """
    Form for adding song data
    """
    class Meta:
        model = Song
        fields = ('title', 'artist', 'lyrics',)
