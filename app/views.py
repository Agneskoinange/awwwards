from django.http.response import Http404, HttpResponseRedirect
from app.forms import CreateProfileForm, NewProjectForm, RatingProjectForm
from django.shortcuts import render, redirect
import datetime as dt
from .models import Profile, Project, Vote
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from app import serializer

# Create your views here.
def index(request):
    date = dt.date.today()
    projects = Project.display_all_projects()

    return render(request, 'index.html', {"date": date, "projects":projects})


@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"projects": searched_projects})
    else:
        message = 'You have not searched for anything'
        return render(request, 'search.html', {'message': message})

def display_all_project(request, project_id):
    try:
        project = Project.objects.get(pk = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, "project.html", {"project":project})
  

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Author = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'add_new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    author = current_user
    projects = Project.get_by_author(author)

    
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = CreateProfileForm()
    
    return render(request, 'profile.html', {"form":form, "projects":projects})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        print(serializers.data)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

