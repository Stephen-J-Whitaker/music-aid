from .models import Song
from django import forms
from django_summernote.widgets import SummernoteWidget


class AddSongForm(forms.ModelForm):
    """
    Form for adding song data
    """
    class Meta:
        model = Song
        fields = ('title', 'artist', 'lyrics',)
        widgets = {
            'lyrics': SummernoteWidget(),
        }
