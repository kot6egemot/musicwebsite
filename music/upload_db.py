import os
import json
import glob
import re
general_path = 'static\sound'
all_album = os.listdir(general_path)
n = 0#id album
k = 0#id track
jsn_1 = []
jsn_2 = []
jsn_3 = []
with open('fixtures/track.json', 'w') as out_one:
    with open('fixtures/album.json', 'w') as out_two:
        for album in all_album:
            n+=1#счетчик номера альбома
            album_path = general_path + '\\' + album

            """
            подгрузка пути к обложке
            """

            cover_image = [i for i in os.listdir(album_path) if '.mp3' not in i]
            path_cover = album_path.split('static')[1] + '\\' + cover_image[0]

            #list album
            jsn_str_2 = {
                            "model": "music.album",
                            "pk": n,
                            "fields": {
                                "title": album,
                                "path_cover": path_cover
                            }
                        }
            #складываем в список записи для переводы в json
            jsn_2.append(jsn_str_2)
            #определение пути для индивидуального альбома
            tracklist = os.listdir(album_path)

            for name_track in tracklist:
                k+=1
                #формирование пути и зачистка '/static'
                path_file_mp3 = album_path.split('static')[1] + '\\' + name_track
                if path_file_mp3.endswith('.mp3'):
                    jsn_str_1 = {
                                    "model": "music.list_track",
                                    "pk": k,
                                    "fields": {
                                      "album": n,
                                      "title": name_track,
                                      "track": path_file_mp3
                                    }
                                }
                    #складываем в список песни для записи в json
                    jsn_1.append(jsn_str_1)
        json.dump(jsn_1, out_one)
        json.dump(jsn_2, out_two)
    out_two.close()
out_one.close()