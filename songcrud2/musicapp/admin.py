from django.contrib import admin
from .models import Artiste,Song,Lyric
from django.contrib import admin

# Register your models here.

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')
    search_fields= ('first_name','last_name')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=('title','artiste','date_released','id')
    search_fields=('title','artiste')

@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display=('song','content','id')
    search_fields=('song',)
