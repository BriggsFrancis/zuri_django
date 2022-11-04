from django.urls import path
from .views import musicapp_list_api,song_detail_api

urlpatterns=[
    path('songslist/',musicapp_list_api,name='songslistapi'),
    path('songslist/<int:id>/',song_detail_api,name='song_detail_api'),
]