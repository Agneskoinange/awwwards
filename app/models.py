import cloudinary
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.http import Http404
from django.db.models import ObjectDoesNotExist 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    prof_pic = CloudinaryField('image', null=True)
    link = models.URLField(default='DEFAULT VALUE')
    email = models.EmailField(default='DEFAULT VALUE')

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def edit_bio(self, new_bio):
        self.bio = new_bio
        self.save()

class Project(models.Model):
    project_title = models.CharField(max_length= 50)
    project_image = CloudinaryField('project_image')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='1')

    def __str__(self) -> str:
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def display_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects

    @classmethod
    def get_by_author(cls,author):
        projects = cls.objects.filter(author=author)
        return projects

    @classmethod
    def get_project(request, id):
        try:
            project = Project.objecs.get(pk = id)
        except ObjectDoesNotExist:
            raise Http404()
        
        return project

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ['-pub_date']

class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = "votes")
    pub_date = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    design = models.FloatField(default=0, blank=True)
    content = models.FloatField(default=0, blank=True)
    usability = models.FloatField(default=0, blank=True)

    def save_vote(self):
        self.save()

    def delete_vote(self):
        self.delete()

    @classmethod
    def get_project_votes(cls, project):
        return cls.objects.filter(project = project)

    @classmethod
    def get_project_voters(cls, project):
        return cls.objects.filter(project = project)

    class Meta:
        ordering = ['-pub_date']