from django.views import View, generic
from .models import Song
from django.shortcuts import render, get_object_or_404


class SongbookList(generic.ListView):
    """
    Class based view to show the users
    songbook list
    """
    model = Song
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Music Aid Songbook'

        return context

    def get_queryset(self):
        if self.request.user.id is not None:
            return Song.objects.filter(user=self.request.user)


# Code supplied by Code Institute Tutor Support
class AddSong(generic.CreateView):
    model = Song
    fields = ('title', 'artist', 'lyrics')
    template_name = 'add_song.html'
    success_url = '/'
    # End of code supplied by Code Institute Tutor Support
