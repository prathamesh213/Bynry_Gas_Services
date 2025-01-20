from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class SupportRepresentative(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_requests = models.ManyToManyField('service_requests.ServiceRequest', blank=True)

    def __str__(self):
        return self.user.username
