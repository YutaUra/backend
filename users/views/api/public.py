from rest_framework import generics
from rest_framework import permissions

from users.serializers import PublicUserSerializer
from users.models import User


class PublicUserDataView(generics.RetrieveAPIView):
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = PublicUserSerializer
    lookup_field = 'pub_id'
    queryset = User.objects.all()