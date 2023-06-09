from . import views
from django.urls import path

handler404 = 'songbook.views.handler404'

urlpatterns = [
     path('', views.SongbookList.as_view(), name='home'),
     path('song_add/', views.SongAdd.as_view(), name='song_add'),
     path('song_view/<int:pk>', views.SongView.as_view(),
          name='song_view'),
     path('song_edit/<int:pk>', views.SongEdit.as_view(),
          name='song_edit'),
     path('song_delete/<int:pk>', views.SongDelete.as_view(),
          name='song_delete'),
     path('setlist_add/', views.SetlistAdd.as_view(),
          name='setlist_add'),
     path('setlist_list/', views.SetlistList.as_view(),
          name='setlist_list'),
     path('setlist_view/<int:pk>', views.SetlistView.as_view(),
          name='setlist_view'),
     path('setlist_edit/<int:pk>', views.SetlistEdit.as_view(),
          name='setlist_edit'),
     path('setlist_delete/<int:pk>',
          views.SetlistDelete.as_view(), name='setlist_delete'),
     path('setlist_song_view/<int:pk>/<int:setlist_pk>',
          views.SongView.as_view(), name='setlist_song_view'),
     path('setlist_song_edit/<int:pk>/<int:setlist_pk>',
          views.SongEdit.as_view(), name='setlist_song_edit'),
     path('setlist_song_delete/<int:pk>/<int:setlist_pk>',
          views.SongDelete.as_view(), name='setlist_song_delete'),
     path('song_title_validate/', views.song_title_validate,
          name='song_title_validate'),
     path('setlist_name_validate/', views.setlist_name_validate,
          name='setlist_name_validate'),
]
