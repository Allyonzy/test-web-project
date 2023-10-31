from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    #       ^-- Change this to anything you like eg:secret
    path('', include('user_sessions.urls', 'user_sessions')),
]
