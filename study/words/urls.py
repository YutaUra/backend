from django.urls import path
from . import views as v

urlpatterns = [
    path('get/', v.WordGetView.as_view()),

    path('answer/', v.WordAnswerView.as_view())
]
