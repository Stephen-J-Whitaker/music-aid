from django.contrib import admin
from .models import Song, Setlist
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Song)
class SongAdmin(SummernoteModelAdmin):
    """
    Song admin registration class
    """
    list_display = ('user', 'title', 'artist')
    search_fields = ['title', 'lyrics']
    summernote_fields = ('lyrics')


@admin.register(Setlist)
class SetlistAdmin(admin.ModelAdmin):
    """
    Setlist admin registration class
    """
    list_display = ('user', 'setlist_name')
