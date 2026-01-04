from django.urls import path
from . import views

urlpatterns = [
    # user
    path('', views.product_list, name='product_list'),
    path('request/<int:product_id>/', views.request_product, name='request_product'),

    # staff
    path('staff/requests/', views.staff_requests, name='staff_requests'),
    path(
        'staff/requests/<int:request_id>/<str:status>/',
        views.update_request_status,
        name='update_request_status'
    ),
]
