from django.urls import path
from .views import FollowToggleApiView

urlpatterns = [
    path("<int:pk>/follow/",FollowToggleApiView.as_view())
]