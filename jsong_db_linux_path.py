import os
import json
import glob
import re

def get_next_listdir(*args):
	pass

def write_json(name,table):
	with open(name, 'w') as file:
		json.dump(table,file)
	file.close()

general_path = 'media/artist'
ARTIST = os.listdir(general_path)

array = dict()

json_table_artist = []
pk_artist = 0
json_table_albums = []
pk_album = 0
json_table_song = []
pk_song = 0

for artist in ARTIST:
	pk_artist+=1
	album_array = {} # dict album:song
	json_table_artist.append(
								{
							    "model": "music.artist",
							    "pk": pk_artist,
							    "fields": {
							        "title": artist,
							    		}
								}	
							)
	for album in os.listdir(os.path.join(general_path, artist)):
		pk_album+=1
		json_table_albums.append(
									{
								    "model": "music.album",
								    "pk": pk_album,
								    "fields": {
										"artist": pk_artist,
								        "title": album,
								        "path_cover": 'none',
						    			}
									}
								)

		album_array[album] = [os.path.join(general_path,artist, album, i)
		 						for i in os.listdir(os.path.join(general_path, artist, album))]

		for path_song in album_array[album]:
			if '.jpg' in path_song:
				path_cover = path_song
				json_table_albums[-1]['fields']['path_cover'] = path_song
			else:
				pk_song+=1
				json_table_song.append(
											{
										    "model": "music.list_track",
										    "pk": pk_song,
										    "fields": {
										    		  "artist": pk_artist,
												      "album": pk_album,
												      "title": os.path.split(path_song)[-1],
												      "path": path_song
												    }
											}
										)									
write_json('music/fixtures/artist.json', json_table_artist)
write_json('music/fixtures/album.json', json_table_albums)
write_json('music/fixtures/song.json', json_table_song)

