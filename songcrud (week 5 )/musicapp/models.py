from datetime import datetime
from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste (models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)


class Song (models.Model):
    artiste=models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    date_released=models.DateField(default=datetime.today)
    likes=models.ManyToManyField(Artiste,blank=True,related_name='likes')
    Artiste_id=models.BigAutoField(primary_key=True) 
    

class Lyric(models.Model):
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    content=models.TextField()
    Song_id=models.BigAutoField(primary_key=True)