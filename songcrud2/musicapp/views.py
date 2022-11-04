from django.shortcuts import render
from .models import Artiste,Song,Lyric

# Create your views here.

def Home(request):
    context={'Song':Song.objects.all(),
                'Artiste':Artiste.objects.all(),
                'Lyrics':Lyric.objects.all(),
    }
    return render(request,'musicapp/songs.html',context)

def detail_page(request,id):
    context={'song':Song.objects.get(id=id),
            'lyrics':Lyric.objects.get(id=id),}
    return render(request,'musicapp/detail.html',context)
