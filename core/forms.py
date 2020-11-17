from django import forms
from django.contrib.auth.models import User
from chat.models import UserProfile

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'books_view_hide_completed', 'reviews_view_hide_others']