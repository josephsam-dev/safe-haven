from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('add/', views.add_story, name='add_story'),
]
