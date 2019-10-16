from django.urls import path, include

urlpatterns = [
    path('word/', include('study.words.urls'))
]
