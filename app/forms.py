from .models import Profile, Project, Vote
from django.forms import ModelForm, widgets
from django import forms
class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
        widgets = {
            'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = [ 'pub_date', 'author']
        widgets = {
          'project_description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        } 

class RatingProjectForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ['pub_date', 'voter', 'project']