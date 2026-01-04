from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("counseling/", views.counseling, name="counseling"),
    path("stories/", views.stories, name="stories"),
    path("shop/", views.shop, name="shop"),
    path("staff/requests/", views.staff_requests, name="staff_requests"),
]
