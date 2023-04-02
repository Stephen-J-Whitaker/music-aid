from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongbookList.as_view(), name='home'),
    path('add_song/', views.AddNewSong.as_view(), name='add_song'),
    path('song_view/<slug:slug>', views.SongView.as_view(),
         name='song_view'),
    path('edit_song/<slug:slug>', views.EditSong.as_view(),
         name='edit_song'),
]
