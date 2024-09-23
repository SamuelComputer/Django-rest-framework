
from django.contrib import admin
from django.urls import path
from .views import index, MovieDetail, MovieViewSet


urlpatterns = [
    path('', index, name= "index"),
    path('drf/', MovieViewSet, name= "drf"),
    path('drf/<int:pk>/', MovieDetail, name= "detail"),
    

]
