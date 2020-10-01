from rest_framework import serializers
from .models import PropertyInfo

class PropertyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyInfo
        fields = '__all__'
