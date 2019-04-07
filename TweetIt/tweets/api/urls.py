from .views import (
        TweetListApiView,
        TweetCreateApiView,
        RetweetAPIView,
        LikeToggleAPIView,
        TweetDeleteApiView,
        TweetSearchApiView
        # TweetNewApiView
)
from django.urls import path

urlpatterns = [
    # path('tweet/new/',TweetNewApiView.as_view()),
    path('tweet/',TweetListApiView.as_view(),name='tweet-api'),
    path('tweet/search/',TweetSearchApiView.as_view(),name='tweet-search-api'),
    path('create/',TweetCreateApiView.as_view()),
    path('<int:pk>/delete/',TweetDeleteApiView.as_view()),
    path('<int:pk>/retweet/',RetweetAPIView.as_view()),
    path('<int:pk>/like/',LikeToggleAPIView.as_view()),
]