from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongbookList.as_view(), name='home'),
    path('add_song/', views.AddSong.as_view(), name='add_song'),
    path('song_view/<int:pk>', views.SongView.as_view(),
         name='song_view'),
    path('edit_song/<int:pk>', views.EditSong.as_view(),
         name='edit_song'),
    path('delete_song/<int:pk>', views.DeleteSong.as_view(),
         name='delete_song'),
]
