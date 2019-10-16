from rest_framework import generics
from users.serializers import FollowRelationSerializer
from users.models import FollowRelation
from django.http import HttpResponseBadRequest


class FollowRelationDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = FollowRelationSerializer
    lookup_field = "follow_user"

    def get_queryset(self):
        return FollowRelation.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        if request.user.pub_id == self.kwargs.get('follow_user'):
            return HttpResponseBadRequest()
        return super().get(request, *args, **kwargs)


class FollowRelationCreateView(generics.CreateAPIView):
    serializer_class = FollowRelationSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        if self.request.user.pub_id != data['user']:
            return HttpResponseBadRequest()
        try:
            fr = FollowRelation.objects.get(user_id=data['user'], follow_user=data['follow_user'])
        except Exception:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseBadRequest()


