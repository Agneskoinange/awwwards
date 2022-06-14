from django.test import TestCase
from .models import Project, Profile, Vote
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User(id=1, username='nessie', password='agnes1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class VoteTestClass(TestCase):
    def setUp(self):
        self.nessie = User(username = "nessie", email = "agnesprojectsemail@gmail.com",password = "agnes1234")
        self.profile = Profile(user= self.agnes, prof_pic='png',bio='bio', email='agnesprojectsemail@gmail.com"', link='www.profile.com')
        self.project = Project(author= "nessie", project_title= "test", project_image = "imageurl", project_description ="test project", link = "testlink")
        self.vote = Vote(voter=self.profile, project=self.project, usability= 4, design= 7, content = 3)

        self.nessie.save()
        self.profile.save_profile()
        self.project.save_project()
        self.vote.save_vote()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()
        Vote.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.vote, Vote))

    def test_save_vote(self):
        votes = Vote.objects.all()
        self.assertTrue(len(votes)> 0)

    def test_delete_vote(self):
        votes1 = Vote.objects.all()
        self.assertEqual(len(votes1),1)
        self.vote.delete_vote()
        votes2 = Vote.objects.all()
        self.assertEqual(len(votes2),0)

    def test_get_project_voters(self):
        voters = Vote.get_project_voters(self.profile)
        self.assertEqual(voters[0].voter.user.username, 'agnes')
        self.assertEqual(len(voters), 1)

    def test_get_project_votes(self):
        votes = Vote.get_project_votes(self.project)
        self.assertEqual(votes[0].design, 7)
        self.assertEqual(len(votes), 1)