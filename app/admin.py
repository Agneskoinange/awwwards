from django.contrib import admin
from .models import Project, Profile, Vote



admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Vote)