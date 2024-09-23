from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from movies import serializers
from .serializers import MovieSerial # type: ignore
from .models import MovieData
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index (request):
    return HttpResponse("Hello API") 



@api_view(["GET", "POST"])
def MovieViewSet(request):
    set = MovieData.objects.all()
    serializer = MovieSerial(set, many =True)
    return Response (serializer.data)



@api_view(["GET", "POST"])
def MovieDetail(request, pk):
    Movie = MovieData.objects.get(id=pk)
    serializer = MovieSerial(Movie)
    return Response (serializer.data)
