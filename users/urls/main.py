from django.urls import path
from users import views

urlpatterns = [
    path('check/id/<str:id>/', views.IsExistId),
    path('check/email/<str:email>/', views.IsExistEmail),
    path('user/create/', views.UserCreateAPI.as_view()),
    path('user/create/verify/', views.UserCreateVerify),
    path('user/info/', views.AuthInfoGetView.as_view()),
    path('user/update/', views.AuthInfoUpdateview.as_view()),
    path('user/follows/', views.UserFollowsGetView.as_view()),
    path('isFollow/<subjectUser>/<objectUser>/', views.IsFollow),
    path('user/pub_data/<str:pub_id>/', views.PublicUserDataView.as_view()),
    path('follow/delete/<str:follow_user>/', views.FollowRelationDeleteView.as_view()),
    path('follow/create/', views.FollowRelationCreateView.as_view()),
    path('profile/update/', views.ProfileUpdateView.as_view()),
    path('profile/read/', views.ProfileReadView.as_view()),
]
