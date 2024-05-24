from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/videos/', include('videos.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
]
