from django.shortcuts import redirect,render,get_object_or_404
from django.urls import reverse_lazy
# Create your views here.
from django.views import generic
from django.views import View
from .models import Tweet

class TweetListView(generic.ListView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/index.html'

class RetweetView(View):
    def get(self,request,pk,*args,**kwargs):
        tweet = get_object_or_404(Tweet,id=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user,tweet)
            return redirect('/')
        else:
            return redirect('/')
    


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
