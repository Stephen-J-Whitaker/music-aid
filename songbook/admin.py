from django.contrib import admin
from .models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'song_slug')
    search_fields = ['title', 'lyrics']
    prepopulated_fields = {'song_slug': ('user', 'title',)}
