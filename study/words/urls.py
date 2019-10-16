from django.urls import path
from . import views as v

urlpatterns = [
    path('<subject>/<textbook_name>/<unit_name>/<chapter_name>/', v.WordGetView.as_view()),
    path('<subject>/<textbook_name>/<unit_name>/', v.WordGetView.as_view()),
    path('<subject>/<textbook_name>/', v.WordGetView.as_view()),

    path('answer/', v.WordAnswerView.as_view())
]
