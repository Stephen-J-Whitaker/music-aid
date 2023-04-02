from .models import Song, Setlist
from django import forms
from django_summernote.widgets import SummernoteWidget


class SongAddForm(forms.ModelForm):
    """
    Form class for adding editing song data
    """
    class Meta:
        model = Song
        fields = ('title', 'artist', 'lyrics',)
        widgets = {
            'lyrics': SummernoteWidget(),
        }


class SetlistAddForm(forms.ModelForm):
    """
    Form class for creating and editing setlists
    """ 
    class Meta:
        Model = Setlist
        fields = ('setlist_name', 'songs_in_setlist',)

    def __init__(self, *args, **kwargs):
        """
        Override SetistAddForm class init so user can be
        passed in as a parameter and used
        """
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        queryset = Song.objects.filter(artist=user).order_by('title')
        choice_list = [(song.pk, songs.title) for song in queryset]

        self.fields['songs_in_setlist'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple(),
            choices=choice_list,
        )