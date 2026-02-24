from django.urls import path
from . import views

app_name = "support_requests"

urlpatterns = [
    path("", views.support_request, name="support"),
    path("success/", views.support_success, name="success"),
]
