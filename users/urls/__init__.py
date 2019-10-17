from django.urls import path, include
from users.views.api.user_create import UserLogin
from rest_framework_jwt.views import verify_jwt_token

from .api import router
from .main import urlpatterns as url1
from users.views import TestView

urlpatterns = [
    *url1,
    path('test/', TestView.as_view()),
    path('auth/', UserLogin.as_view()),
    path('auth/verify/', verify_jwt_token),
    path('users/', include(router.urls)),
]
