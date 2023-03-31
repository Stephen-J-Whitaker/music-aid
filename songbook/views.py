from django.shortcuts import render
from django.views import view


class SongbookList(View):
    """
    Class based view to show the users
    songbook list
    """
    template_name = "index.html"
