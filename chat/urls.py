  
from django.urls import path, re_path
from .views import index, room
from django.contrib import admin


app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    
]