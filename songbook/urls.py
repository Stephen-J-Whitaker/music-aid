from . import views
from django.urls import path


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
]
