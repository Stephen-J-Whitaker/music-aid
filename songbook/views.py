from django.views import View, generic
from .models import Song


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
        return Song.objects.filter(user=self.request.user)

    # def get(self, request):
    #     """
    #     Show the home page
    #     """

    #     title = "Testify"

    #     return render(
    #         request,
    #         "index.html",
    #         {
    #             "title": title,
    #         }
    #     )
