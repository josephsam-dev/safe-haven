from django.urls import path
from . import views  # This is correct because views.py is in the same app folder

urlpatterns = [
    path('', views.home, name='home'),  # Example route
]
