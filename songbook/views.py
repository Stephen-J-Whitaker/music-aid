from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from .models import Song
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify


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
class AddSong(LoginRequiredMixin, generic.CreateView):
    model = Song
    fields = ('title', 'artist', 'lyrics')
    template_name = 'add_song.html'
    success_url = '/'
    # End of code supplied by Code Institute Tutor Support

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a songs lyrics to songbook'
        return context

    def form_valid(self, form):
        print("this is my comment", form.instance.title)
        form.instance.user = self.request.user
        slug = str(form.instance.user.id) + ' ' + form.instance.title
        print("slug ", slug)
        form.instance.song_slug = slugify(slug)
        print("slugified", form.instance.song_slug)
        return super().form_valid(form)

