from django.contrib import admin
from django.urls import path, include

from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('logout/',auth_views.LogoutView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]