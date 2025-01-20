# gas_utility_project/urls.py
from django.contrib import admin
from django.urls import path, include
from service_requests import views as service_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include('service_requests.urls')),
    path('', service_views.home, name='home'),  # This line will serve the home page
]
