from rest_framework import serializers
from .models import Scans

class subDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scans
        fields = ["scanname", "domains" , "created_at", "user"]