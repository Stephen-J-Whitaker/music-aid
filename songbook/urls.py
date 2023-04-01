from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongbookList.as_view(), name='home'),
    path('add-song/', views.AddSong.as_view(), name='add_song'),
]
