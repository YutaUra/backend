from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from users.serializers import UserFollow
from users.models import User
from users.models import FollowRelation


@api_view(http_method_names=['GET'])
@permission_classes(permission_classes=[permissions.AllowAny])
def IsFollow(request, subjectUser, objectUser):
    if request.method == 'GET':
        sUser = User.objects.get(pub_id=subjectUser)
        try:
            sUser.follows.get(follow_user__pub_id=objectUser)
        except FollowRelation.DoesNotExist:
            data = {
                'result': False
            }
        else:
            data = {
                'result': True
            }

        return Response(data, status.HTTP_200_OK)




class UserFollowsGetView(generics.ListAPIView):
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = UserFollow

    def get_queryset(self):
        pub_id = self.request.query_params.get('id', None)
        if pub_id:
            return User.objects.all().filter(pub_id=pub_id)
        else:
            return User.objects.none()
