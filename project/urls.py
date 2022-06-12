from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include("app.urls")),
]