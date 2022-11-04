from django.db import models
from django.utils import timezone
from django.db import models

# Create your models here.

class Artiste (models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.first_name 

class Song (models.Model):
    artiste=models.ForeignKey(Artiste, on_delete=models.CASCADE, default='1')
    title=models.CharField(max_length=200)
    date_released=models.DateField(default=timezone.now) 
    likes=models.ManyToManyField(Artiste,blank=True,related_name='likes')  
    id=models.AutoField(primary_key=True)    

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-date_released',)



class Lyric(models.Model):
    song=models.OneToOneField(Song,on_delete=models.CASCADE)
    content=models.TextField()
    id=models.BigAutoField(primary_key=True, blank=True)

    def __str__(self):
        return self.content