from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response

class FollowToggleApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk,format=None):
        user = User.objects.filter(pk=pk).first()
        print('*'*10)
        print(user)
        message = "not allowed"
        if request.user.is_authenticated:
            following = request.user.user_profile.get_following()
            if user not in following:
                request.user.user_profile.following.add(user)
                message = "Following"
                return Response({"message":message})
            else:
                request.user.user_profile.following.remove(user)
                message = "Follow"
                return Response({'message':message})
        return Response({"message":message},status=400)
        

# class LikeToggleAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self,request,pk,format=None):
#         tweet_qs = Tweet.objects.filter(pk=pk)
#         message = "Not Allowed"
#         if request.user.is_authenticated:
#             is_liked = Tweet.objects.like_toggle(request.user,tweet_qs.first())
#             return Response({'liked':is_liked})
#         return Response({"message":message},status=400)