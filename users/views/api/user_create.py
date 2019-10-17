from django.db import transaction
from django.conf import settings
from django.core.signing import dumps, loads, BadSignature, SignatureExpired
from django.contrib.auth.models import Group
from django.template.loader import get_template
from django.utils.datetime_safe import datetime
from rest_framework import permissions, generics

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_response_payload_handler
from rest_framework_jwt.views import JSONWebTokenAPIView

from users.models import User
from users.serializers import UserSerializer


@api_view(http_method_names=['GET'])
@permission_classes(permission_classes=[permissions.AllowAny])
def IsExistId(request, id):
    if request.method == 'GET':
        if not id:
            return Response({
                'pub_id': id,
                'errors': ['idがありません。']}, status.HTTP_400_BAD_REQUEST)
        data = {'pub_id': id}
        if User.objects.is_exist_id(id):
            data['used'] = True
        else:
            data['used'] = False
        return Response(data, status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
@permission_classes(permission_classes=[permissions.AllowAny])
def IsExistEmail(request, email):
    if request.method == 'GET':
        if not email:
            return Response({
                'email': email,
                'errors': ['emailがありません。']}, status.HTTP_400_BAD_REQUEST)
        data = {'email': email}
        if User.objects.is_exist_email(email):
            data['used'] = True
        else:
            data['used'] = False
        return Response(data, status.HTTP_200_OK)


class UserCreateAPI(generics.CreateAPIView):
    permission_classes = (
        permissions.AllowAny,
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        no_active = User.objects.filter(is_active=False)
        no_active.filter(pub_id=request.data.get('pub_id')).delete()
        no_active.filter(email=request.data.get('email')).delete()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            # set Group Teacher or Student
            if user.get_user_position() == 'T':
                group = Group.objects.get(name='teacher')
                group.user_set.add(user)
                group.save()
            elif user.get_user_position() == 'S':
                group = Group.objects.get(name='student')
                group.user_set.add(user)
                group.save()

            # アクティベーションURLの送付
            context = {
                'protocol': settings.FRONTEND_POINT.get('PROTOCOL'),
                'domain': settings.FRONTEND_POINT.get('DOMAIN'),
                'token': dumps(user.pk),
                'user': user,
                'site_name': settings.SITE_NAME,
            }

            subject = get_template('users/mails/user_create/subject.txt').render(context)
            message = get_template('users/mails/user_create/message.txt').render(context)

            user.email_user(subject, message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
@permission_classes(permission_classes=[permissions.AllowAny])
def UserCreateVerify(request):
    if request.method == 'POST':
        token = request.data.get('token')
        try:
            user_pk = loads(token, max_age=60 * 60)
        # 例外処理
        # 期限切れ, バッドトークン
        except (SignatureExpired, BadSignature):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # トークンは問題なし
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return Response(status.HTTP_400_BAD_REQUEST)
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                return Response(status=status.HTTP_200_OK)


class UserLogin(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            if not user.is_active:
                return Response(data={'message': 'アクティベートされていません'}, status=status.HTTP_400_BAD_REQUEST)
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
