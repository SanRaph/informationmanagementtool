from rest_framework import serializers
from infomanager.models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
