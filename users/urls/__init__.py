from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from .api import router
from .main import urlpatterns as url1
from users.views import TestView

urlpatterns = [
    *url1,
    path('test/', TestView.as_view()),
    path('auth/', obtain_jwt_token),
    path('auth/verify/', verify_jwt_token),
    path('users/', include(router.urls)),
]
