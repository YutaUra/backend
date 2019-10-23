from django.urls import path, include
from . import views as v

urlpatterns = [
    path('get/textbook/<subject>/', v.TextbookGetView.as_view()),
    path('get/unit/', v.TextbookUnitGetView.as_view()),
    path('get/chapter/', v.TextbookChapterGetView.as_view()),
    path('get/session/', v.get_word_session),
    path('word/', include('study.words.urls'))
]
