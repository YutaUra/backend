from rest_framework import serializers
from users.models import FollowRelation


class FollowRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRelation
        fields = (
            'user',
            'follow_user'
        )

