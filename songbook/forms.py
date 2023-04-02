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
        model = Setlist
        fields = ('setlist_name', 'songs_in_setlist',)

    def __init__(self, *args, **kwargs):
        """
        Override SetistAddForm class init so user can be
        passed in as a parameter and used
        """
        user = kwargs['initial']['user']
        super().__init__(*args, **kwargs)
        print("user ", user)
        queryset = Song.objects.filter(user=user).order_by('title')
        print(" queryset ", queryset)
        choice_list = [(song.pk, song.title) for song in queryset]
        print("choice list", choice_list)
        self.fields['songs_in_setlist'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple(),
            choices=choice_list,
        )
