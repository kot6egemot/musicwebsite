from django import forms
from .models import Playlist
class Form_create_playlist(forms.ModelForm):
	class Meta:
		model = Playlist
		fields = ['title']
		labels = {'title':'Введи название плейлиста'}

class Form_add_song(forms.ModelForm):
	id_track_model = forms.CharField(max_length=20)
	class Meta:
		model = Playlist
		fields = ['title']
		labels = {'title':'Название плейлиста'}

class Form_del_song(forms.ModelForm):
	id_track = forms.CharField()
	# name_playlist = forms.CharField()
	class Meta:
		model = Playlist
		fields= ['title']

class Form_del_pl(forms.ModelForm):
	class Meta:
		model = Playlist
		fields= ['title']

