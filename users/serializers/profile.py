from rest_framework import serializers
from users.models import Profile


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'nickname',
            'icon',
            'user',
            'follows'
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'nickname',
            'icon',
            'user',
            'follows'
        )


class SecretProfileSerializer(BaseProfileSerializer):
    class Meta:
        model = Profile
        fields = (
            'icon',
            'nickname',
            'first_name',
            'last_name',
            'phone',
            'gender',
        )
