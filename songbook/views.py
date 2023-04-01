from django.views import View, generic
from .models import Song
from django.shortcuts import render, get_object_or_404
from songbook.forms import AddSong


class SongbookList(generic.ListView):
    """
    Class based view to show the users
    songbook list
    """
    model = Song
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Music Aid Songbook"

        return context

    def get_queryset(self):
        if self.request.user.id is not None:
            return Song.objects.filter(user=self.request.user)


class AddSong(View):
    """
    Class based form view for adding song data
    """

    def get(self, request, *args, **kwargs):
        add_song_form = AddSong()
        print(add_song_form)
        title = "Add a songs lyrics to songbook"

        return render(
            request,
            "add_song.html",
            {
                'title': title,
                'add_song_form': AddSong()
            },
        )

    def post(self, request, *args, **kwargs):

        add_song_form = AddSong()

        return render(
            request,
            "add_song.html",
            {
                "add_song_form": AddSong(),
            }
        )
