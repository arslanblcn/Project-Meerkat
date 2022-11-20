from django.db import models
from django.contrib.auth.models import User

class Scans(models.Model):
    scanname=models.CharField(max_length=60)
    domains = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.scanname

