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
    Form class for creating setlists
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
        queryset = Song.objects.filter(user=user).order_by('title')
        choice_list = [(song.pk, song.title) for song in queryset]

        self.fields['songs_in_setlist'] = forms.MultipleChoiceField(
            choices=choice_list,
            widget=forms.CheckboxSelectMultiple,
        )


class SetlistEditForm(forms.ModelForm):
    """
    Form class for editing setlists
    """
    class Meta:
        model = Setlist
        fields = ('setlist_name', 'songs_in_setlist',)

    def __init__(self, *args, **kwargs):
        """
        Override SetistAddForm class init so user can be
        passed in as a parameter and used
        """
        user = kwargs.pop('user', None)
        setlist_pk = kwargs.pop('setlist_pk', None)
        super().__init__(*args, **kwargs)
        queryset = Song.objects.filter(user=user).order_by('title')
        choice_list = [(song.pk, song.title) for song in queryset]

        setlist_object = Setlist.objects.get(pk=setlist_pk)
        setlist_songs = setlist_object.songs_in_setlist.all()
        setlist_songs_pks = [song.pk for song in setlist_songs]
        self.fields['setlist_name'] = forms.CharField(
            initial=setlist_object.setlist_name,
        )
        self.fields['songs_in_setlist'] = forms.MultipleChoiceField(
            initial=setlist_songs_pks,
            choices=choice_list,
            widget=forms.CheckboxSelectMultiple,
        )
