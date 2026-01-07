from django.urls import path
from . import views

urlpatterns = [
    # client
    path("book/", views.book_counseling, name="book_counseling"),

    # staff
    path("staff/sessions/", views.staff_sessions, name="staff_sessions"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_counseling, name='book_counseling'),
    path('my-sessions/', views.my_sessions, name='my_sessions'),  # ✅ ADD THIS
    path('staff/sessions/', views.staff_sessions, name='staff_sessions'),
]
