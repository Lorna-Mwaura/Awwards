from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # configuration
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class uploadform(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['image', 'title', 'detail_desciption','url']
