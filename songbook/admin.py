from django.contrib import admin
from .models import Song
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Song)
class SongAdmin(SummernoteModelAdmin):
    list_display = ('user', 'title', 'artist')
    search_fields = ['title', 'lyrics']
    summernote_fields = ('lyrics')
