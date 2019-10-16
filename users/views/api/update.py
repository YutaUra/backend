from django.contrib.auth import authenticate
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from users.serializers import UserSerializer
from users.models import User


class AuthInfoUpdateview(generics.UpdateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = UserSerializer
    lookup_field = 'email'
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user.email)
            return instance
        except User.DoesNotExist:
            raise Http404
