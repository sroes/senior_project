
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from core.forms import ProfileForm
from django.urls import reverse
from chat.models import UserProfile
from django.contrib.auth.decorators import login_required

import json

def checkAuth(request):
    if(request.user.is_authenticated):
        return True
    else:
        return False


def index(request):

    return render(request, 'chat/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })

@login_required(login_url='/login/')
def createProfile(request):
    #instance = get_object_or_404(UserProfile, user=request.user)
   # profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form_instance = ProfileForm(request.POST, request.FILES)
        if(form_instance.is_valid()):
            instance = form_instance.save(commit=False)
            instance.user = request.user
            username = instance.user.username
            instance.save()
            return redirect('profile', username=username)
    else:
        form_instance = ProfileForm()
    context = {
        "form": form_instance,
        "profile": profile,
        "is_user": checkAuth(request),
        "user": request.user,
    }
    return render(request, 'chat/createProfile.html', context=context)

@login_required(login_url='/login/')
def profile(request, username=None):
    use_info = User.objects.filter(username=username)
    person = UserProfile.objects.filter(user=use_info)
   
    profile = UserProfile.objects.filter(user=request.user)


    return render(request, 'chat/profile.html', )