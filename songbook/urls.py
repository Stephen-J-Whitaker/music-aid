from . import views
from django.urls import path


urlpatterns = [
    path('', views.SongbookList.as_view(), name='home'),
]