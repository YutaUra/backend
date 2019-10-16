from rest_framework import permissions, generics
from rest_framework import status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class AuthInfoGetView(generics.RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(data={
            'user_id': request.user.pub_id,
            'email': request.user.email,
            'nickname': request.user.profile.nickname,
            'icon': request.user.profile.icon,
        },
            status=status.HTTP_200_OK)
