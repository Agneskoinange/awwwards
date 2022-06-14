from app.models import Project
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name= 'index'),
    path('search_projects/', views.search_projects, name='search_results'),
    path('project/<project_id>', views.display_all_project, name='project'),
    path('new/project', views.new_project, name='new_project'),
    path('profile/', views.user_profiles, name='profile'),
    path('ratings/',include('star_ratings.urls',namespace='ratings')),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('logout/',auth_views.LogoutView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('project/<post>', views.project, name='project'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)