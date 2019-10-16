from rest_framework import generics
from rest_framework.response import Response

from users.models import Profile
from users.serializers import SecretProfileSerializer


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = SecretProfileSerializer

    def get_queryset(self):
        query_set = Profile.objects.get(user=self.request.user)
        return query_set

    def get_object(self):
        queryset = self.get_queryset()
        print(queryset)
        return queryset


class ProfileReadView(generics.views.APIView):

    serializer_class = SecretProfileSerializer

    def get(self, request):
        obj = self.get_object()
        serializer = self.serializer_class
        data = serializer(obj).data
        return Response(data)

    def get_queryset(self):
        query_set = Profile.objects.get(user=self.request.user)
        return query_set

    def get_object(self):
        queryset = self.get_queryset()
        print(queryset)
        return queryset
