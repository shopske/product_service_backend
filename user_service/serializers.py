from rest_framework import serializers
from user_service.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Product serializer."""
    class Meta:
        model = UserProfile
        fields = '__all__'

