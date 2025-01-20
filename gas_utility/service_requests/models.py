from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('INSTALLATION', 'Installation'),
        ('REPAIR', 'Repair'),
        ('BILLING', 'Billing Inquiry'),
        ('OTHER', 'Other'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    files = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.status}"
