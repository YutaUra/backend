from django.urls import path
from . import views as v

urlpatterns = [
    path('get/', v.WordGetView.as_view()),
    path('get/mode/', v.WordModeGetView.as_view()),
    path('review/', v.WordReviewView.as_view()),

    path('answer/', v.WordAnswerView.as_view())
]
