from django.urls import path
from .views import (
    TweetListView,
    TweetDetailView,
    RetweetView,
    TweetDeleteView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(TweetListView.as_view()),name='tweet'),
    path('<int:pk>/tweet/',login_required(TweetDetailView.as_view()),name='tweet-detail'),
    path('<int:pk>/delete/',login_required(TweetDeleteView.as_view()),name='tweet-delete'),
    path('<int:pk>/retweet/',login_required(RetweetView.as_view()),name='retweet'),
]