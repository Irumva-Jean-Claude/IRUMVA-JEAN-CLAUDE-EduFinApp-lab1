from rest_framework import serializers
from core.models import Testing

class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'
class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields=['id','name']