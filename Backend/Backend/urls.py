from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('', include('user_sessions.urls', 'user_sessions')),
    path('account/', include('allauth.urls')),
]
