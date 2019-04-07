from django.shortcuts import redirect,render,get_object_or_404
from django.urls import reverse_lazy
# Create your views here.
from django.contrib import messages
from django.views import generic
from django.views import View
from django.db.models import Q 
from django.contrib.auth.models import User
from .models import Tweet
from users.models import Follow

class TweetListView(generic.ListView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/index.html'

    def get_queryset(self,*args,**kwargs):
        print(self.request.GET)
        return Tweet.objects.all()

    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        # context['Follow_User'] = User.objects.exclude(
        #     Q(user__in = self.request.user.user_profile.following.all())
        # )
        # print(context['Follow_User'])
        all_users = User.objects.all()
        following_user = self.request.user.user_profile.following.all()
        follow_user = []
        for user in all_users:
            if user not in following_user and user!=self.request.user:
                follow_user.append(user)
        context['follow_user'] = follow_user
        return context

class RetweetView(View):
    def get(self,request,pk,*args,**kwargs):
        tweet = get_object_or_404(Tweet,id=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user,tweet)
            return redirect('/')
        else:
            return redirect('/')

class TweetSearchView(generic.ListView):
    template_name = 'tweets/search.html'
    queryset = Tweet.objects.all()


class TweetDetailView(generic.DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/tweet_detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super(TweetDetailView,self).get_context_data(*args,**kwargs)
        pk = self.kwargs.get('pk')
        return context

class TweetDeleteView(generic.DeleteView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/tweet_delete.html'
    success_url = '/'
