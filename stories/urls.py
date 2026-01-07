from django.urls import path
from .views import story_list, add_story, offer_support

urlpatterns = [
    path("", story_list, name="stories"),
    path("add/", add_story, name="add_story"),
    path("offer-support/<int:story_id>/", offer_support, name="offer_support"),
]
