from django.shortcuts import render, redirect, get_object_or_404
from .forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from chat.models import UserProfile
from core.forms import ProfileFriends
from friends.models import FriendRequest, Profile
from django.contrib.auth.decorators import login_required


def home(request):
    friends = []
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        friends = profile.friends.all()

    context = {
        "friends_list": friends,
    } 
    return render(request, 'core/home.html', context=context)




def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB

            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            #UserProfile.objects.get_or_create(user=user)
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            print(join_form.errors)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)
    
    join_form = JoinForm()
    context = {
        "user": request.user,
        "join_form": join_form,
    }
    return render(request, 'core/join.html', context=context)


def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(request, username=username, password=password)
            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        #Nothing has been provided for username or password.
        return render(request, 'core/login.html', {"login_form": LoginForm})

@login_required(login_url='/login/')
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")

def about(request):
    return render(request, 'core/about.html')

@login_required(login_url='/login/')
def createProfile(request):
    instance = get_object_or_404(UserProfile, user=request.user)
    profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form_instance = ProfileForm(request.POST, request.FILES, instance=instance)
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
    return render(request, 'core/createProfile.html', context=context)

@login_required(login_url='/login/')
def profile(request, username=None):
    num_pages = 0
    num_pages_overall = 0
    use_info = User.objects.get(username=username)
    person = UserProfile.objects.get(user=use_info)
    pic = person.picture.url
    profile = UserProfile.objects.get(user=request.user)


    return render(request, 'core/profile.html', context=context)
