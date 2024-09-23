from rest_framework import serializers
from .models import MovieData




class MovieSerial(serializers.ModelSerializer):
    class Meta :
        model = MovieData
        fields = "__all__"