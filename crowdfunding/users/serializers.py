from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'password',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_img',
            'user_desc',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
            ]
        extra_kwargs = {
            'username': {'write_only': True},
            'password': {'write_only': True},
            'email': {'write_only': True},
            }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)