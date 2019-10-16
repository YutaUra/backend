from rest_framework import serializers
from users.models import User
from .profile import BaseProfileSerializer


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pub_id',
            'nickname',
            'icon',
        )


class PublicUserSerializer(BaseUserSerializer):
    is_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pub_id',
            'nickname',
            'icon',
            'is_following',
        )

    def get_is_following(self, instance):
        user = self.context.get('request').user
        if str(user) == 'AnonymousUser':
            return False
        return instance.get_is_following(user)


class BaseUsersSerializer(serializers.ListSerializer):
    child = PublicUserSerializer()


class UserFollow(BaseUserSerializer):
    get_follows = BaseUsersSerializer()
    get_follower = BaseUsersSerializer()

    class Meta:
        model = User
        fields = (
            'pub_id',
            'get_follows',
            'get_follower'
        )


class UserSerializer(serializers.ModelSerializer):
    # profile = BaseProfileSerializer()
    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'pub_id',
            'email',
            'password',
            '_position',
        )

    def create(self, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        return User.objects.create_user(email, password, **validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
