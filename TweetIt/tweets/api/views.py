from rest_framework import generics
from tweets.models import Tweet
from .serializers import TweetModelSerializer
from rest_framework import permissions
from django.db.models import Q
from django.utils import timezone
from users.models import Follow
from rest_framework.views import APIView
from rest_framework.response import Response


class TweetDeleteApiView(generics.DestroyAPIView):
    queryset = Tweet.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TweetModelSerializer

class TweetListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TweetModelSerializer

    # def get_serializer(self,*args,**kwargs):
    #     context = super(TweetListApiView,self).get_serializer(*args,**kwargs)
    #     #print(context)
    #     #context['request'] = self.request
    #     return context

    def get_serializer_context(self,*args,**kwargs):
        context = super(TweetListApiView,self).get_serializer_context(*args,**kwargs)
        context['request'] = self.request
        return context 

        
    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get("q" or None)
        im_following = self.request.user.user_profile.get_following()
        qs1 = Tweet.objects.filter(Q(user__in=im_following))
        qs2 = Tweet.objects.filter(user=self.request.user)
        qs = (qs1 | qs2).distinct().order_by("-date_posted")

        return qs

class TweetCreateApiView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk,format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "Not Allowed"
        print(tweet_qs)
        if tweet_qs.exists() and tweet_qs.count() == 1:
            new_tweet = Tweet.objects.retweet(request.user,tweet_qs.first())
            if new_tweet is not None:
                data = TweetModelSerializer(new_tweet).data
                return Response(data)
        message = "Cannot retweet same in 1 day."
        return Response({"message":message},status=400)


class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk,format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "Not Allowed"
        if request.user.is_authenticated:
            is_liked = Tweet.objects.like_toggle(request.user,tweet_qs.first())
            return Response({'liked':is_liked})
        return Response({"message":message},status=400)