from django.shortcuts import render, redirect
from django.contrib import messages
from .serializers import ProjectSerializer
from .forms import UserRegistrationForm, uploadform
from django.contrib.auth.decorators import login_required
from .models import Project
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
def welcome(request):
    projects = Project.objects.all()
    return render(request,'welcome.html', {"projects":projects})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('login') # Redirect user to Homepage
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

@login_required # Require user logged in before they can access profile page
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def upload(request):
    '''
    function to upload project for display
    '''
    current_user = request.user
    if request.method == "POST":
        form = uploadform(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect('welcome')
    else:
        form = uploadform()
    context = {
        "form":form
    }

    return render(request,"projects/upload.html",context)

class ProjectList(viewsets.ModelViewSet):
        queryset = Project.objects.all().order_by('title')
        serializer_class =ProjectSerializer
