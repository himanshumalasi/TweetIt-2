from django.urls import path
from .views import (
    UserDetailView,
    UserFollowingView,
    UserFollowerView,
    userfollow,
    profile
)

urlpatterns = [
    path('follow/<slug:username>',userfollow,name='user-follow'),
    path('following/<slug:username>',UserFollowingView.as_view(),name='user-following'),
    path('follower/<slug:username>',UserFollowerView.as_view(),name='user-follower'),
    path('profile/',profile,name='profile'),
    path('<slug:username>/',UserDetailView.as_view(),name='user-detail'),
]