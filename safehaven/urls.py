from django.contrib import admin
from django.urls import path, include  # include allows you to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Connect your 'main' app URLs
]
