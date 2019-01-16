from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Album, List_track, Playlist
from .forms import Form_create_playlist, Form_add_song, Form_del_song, Form_del_pl

"""
По базе данных:
Исполнители -> Альбомы + пути до файлов -> имена файлов по альбомно
Юзеры -> их плейлисты
"""

def index_mus(request):
    return render(request, 'music/base.html')

def mus_album_table(request):
    album = Album.objects.all()
    context = {'album' : album}
    return render(request, 'music/m_albums.html',context)
#Страница альбома
def self_album(request, album_title):
    """
    Рендерим стрницу альбома(запрашиваем все песни)
    Рисуем форму для обработки добавления песни в пользовательский плейлист
    Испраивать дубликаты записей в базе данных
    """

    all_user_pl = Playlist.objects.all()
    album = Album.objects.get(title = album_title)
    #получить все записи через вшений ключ model.name_model _set .all()
    tracks = album.list_track_set.all()

    #Создаем и обрабатываем форму
    if request.method != 'POST':
        form = Form_add_song()
    else:
        form = Form_add_song(request.POST)
        if form.is_valid():
            s_form = form.save(commit = False)

            data = (request.POST['title'], request.POST['id_track_model'])#В поле title вставляется id 
            playlist = Playlist.objects.get(id = data[0])
            song = List_track.objects.get(id = data[1])

            playlist.pl_and_lt.add(song)

    context = {'album': album,
               'tracks':tracks,
               'form':form,
               'all_user_pl':all_user_pl,
               }
    return render(request, 'music/self_album.html', context)

def user_account(request):
    pl = (request.user).playlist_set.all()#получение плейлистов юзера для вывода в шаблон
    #работа с данными через форму
    songs_pl=''
    active_pl =''
    form_del_song = Form_del_song()
    form_del_pl = Form_del_pl()

    if request.method != 'POST':
        form = Form_create_playlist()


        #Получение списка пл_листов
        if len(request.GET) != 0:
            active_pl = request.GET['pl']

            active_pl = Playlist.objects.get(title=active_pl)
            
            songs_pl = active_pl.pl_and_lt.all() #получение связей через поле many to many
    else:

        form = Form_create_playlist(request.POST)
        if form.is_valid():
            new_playlist = form.save(commit=False)
            title = request.POST['title']   
            if ( (len(Playlist.objects.filter(title = title)) < 1 )):
                new_playlist.owner = request.user
                new_playlist.save()


    context = {'form': form,
                'form_del_pl':form_del_pl,
               'form_del_song':form_del_song,       
               'user_playlist': pl,
               'songs_pl':songs_pl,
               'active_pl': active_pl}

    return render(request, 'music/user_account.html', context)

def del_pl(request):
    form_del_pl = Form_del_pl(request.POST)
    if form_del_pl.is_valid():
        form_del_pl = form_del_pl.save(commit = False)
        p = Playlist.objects.get(id=request.POST['title'])
        p.delete()
    return HttpResponseRedirect('/index/profile')   

def del_song(request):
    form_del_song = Form_del_song(request.POST)
    if form_del_song.is_valid():
        form_del_song = form_del_song.save(commit=False)
        p = Playlist.objects.get(title = request.POST['title'])#
        t = List_track.objects.get(id = request.POST['id_track'])
        p.pl_and_lt.remove(t)
        return HttpResponseRedirect('/index/profile')   
