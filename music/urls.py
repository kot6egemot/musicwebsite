from django.urls import path
from .views import index_mus,\
    mus_album_table, \
    self_album, \
    user_account, del_pl, del_song

app_name = 'music'

urlpatterns = [
    path('', index_mus, name = 'index' ),
    path('music_albums/', mus_album_table, name = 'm_albums'),
    path('music_albums/<str:album_title>/', self_album),
    path('profile/', user_account, name='user_account'),
    path('profile/del_pl', del_pl),
    path('profile/del_song', del_song),
]
