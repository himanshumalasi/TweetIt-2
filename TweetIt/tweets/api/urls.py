from .views import (
        TweetListApiView,
        TweetCreateApiView,
        RetweetAPIView,
        LikeToggleAPIView,
        TweetDeleteApiView
        # TweetNewApiView
)
from django.urls import path

urlpatterns = [
    # path('tweet/new/',TweetNewApiView.as_view()),
    path('tweet/',TweetListApiView.as_view()),
    path('create/',TweetCreateApiView.as_view()),
    path('<int:pk>/delete/',TweetDeleteApiView.as_view()),
    path('<int:pk>/retweet/',RetweetAPIView.as_view()),
    path('<int:pk>/like/',LikeToggleAPIView.as_view()),
]