from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT

from.serializers import SongSerializer
from django.views.decorators.csrf import csrf_exempt
from musicapp.models import Song

@api_view(['GET','POST'])
def musicapp_list_api(request):
    if request.method=='GET':
        songs=Song.objects.all()

        serializer=SongSerializer(songs, many=True)  # many=True is due to the fact that we are returning a query set not a singular item
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method=='POST':
        #data=JSONParser().parse(request)
        serializer=SongSerializer(data=request.data ) ## data brefore)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def song_detail_api(request,id):
    try:
        song=Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response({'message':'Song Not Found'},status=HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=SongSerializer(song) 
        return Response(serializer.data, status=HTTP_200_OK)

    if request.method=='PUT':  #### to update
        serializer=SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        song.delete()
        return Response({'message':'Song deleted'}, status=HTTP_204_NO_CONTENT)