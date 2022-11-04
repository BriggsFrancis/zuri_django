from rest_framework import serializers

from musicapp.models import Song,Artiste

class SongSerializer (serializers.ModelSerializer):
    artiste_first_name= serializers.ReadOnlyField(source='artiste.first_name')
    artiste_last_name= serializers.ReadOnlyField(source='artiste.last_name')
    
    
    class Meta:
        model= Song
        fields=['artiste_first_name','artiste_last_name','title','date_released']

 