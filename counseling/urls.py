from django.urls import path
from . import views

urlpatterns = [
    path("", views.session_list, name="counseling"),
    path("book/", views.book_counseling, name="book_counseling"),
    path("my-sessions/", views.my_sessions, name="my_sessions"),
    path("staff/sessions/", views.staff_sessions, name="staff_sessions"),
]
