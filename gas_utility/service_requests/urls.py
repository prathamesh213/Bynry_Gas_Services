from django.urls import path
from . import views

app_name = 'service_requests'

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('status/<int:pk>/', views.request_status, name='request_status'),
]
