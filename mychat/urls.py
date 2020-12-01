"""mychat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from core import views as core_views
from friends import views as friends_views
from chat import views as chat_views
from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView



urlpatterns = [
    path('', core_views.home, name='home'),
    path('chat/', include('chat.urls')),
    path('friends/', include('friends.urls')),

    path('users/', include('friends.urls')),
    
    path('users/<slug>/', friends_views.profile_view, name='profile_view'),
   # path('friends/', friends_views.friends, name='friends'),
    path('admin/', admin.site.urls),
    path('login/', core_views.user_login, name='login'),
    path('logout/', core_views.user_logout, name='user_logout'),
    path('join/', core_views.join, name='join'),

    #path('profile/', core_views.profile, name='profile'),
    path('createProfile/', chat_views.createProfile, name='createProfile'),
    path('profile/<username>/', chat_views.profile, name='profile'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
   # re_path(r'^.*', TemplateView.as_view(template_name='index.html'))
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)