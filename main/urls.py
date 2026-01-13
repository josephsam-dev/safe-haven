from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("shop/", views.shop, name="shop"),
    path("staff/requests/", views.staff_requests, name="staff_requests"),
    path("about/", views.about, name="about"),
    path("mission/", views.mission, name="mission"),

]
