from django.shortcuts import render
from django.views import View


class SongbookList(View):
    """
    Class based view to show the users
    songbook list
    """
    template_name = "index.html"

    def get(self, request):
        """
        Show the home page
        """

        title = "Music Aid Songbook"

        return render(
            request,
            "index.html",
            {
                "title": title,
            }
        )
