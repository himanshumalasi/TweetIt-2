from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic,View
from django.contrib.auth.models import User
from .models import Follow
from .forms import UserRegisterForm, UserProfileForm


class UserDetailView(generic.DetailView):
    queryset = User.objects.all()
    template_name = 'users/user_detail.html'

    def get_object(self):
        return get_object_or_404(User,username__iexact=self.kwargs.get("username"))

class UserFollowingView(generic.ListView):
    template_name = 'users/following.html'
    queryset = User.objects.all()
    request_user = ''

    def get(self,request,*args,**kwargs):
        user_request = kwargs.get('username')
        self.request_user = user_request
        return super(UserFollowingView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserFollowingView,self).get_context_data(**kwargs)
        context['request_user'] = User.objects.get(username=self.request_user)
        context['following'] = get_object_or_404(User,username__iexact=self.request_user).user_profile.following.all()
        print(context)
        return context

class UserFollowerView(generic.ListView):
    template_name = 'users/followers.html'
    queryset = User.objects.all()
    request_user = ''

    def get(self,request,*args,**kwargs):
        self.request_user = kwargs.get('username')
        return super(UserFollowerView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(UserFollowerView,self).get_context_data(**kwargs)
        context['request_user'] = User.objects.get(username=self.request_user)
        context['follower'] = get_object_or_404(User,username__iexact=self.request_user).followed_by.all()
        #context['follower'] = self.request.user.followed_by.all()
        print(context)
        return context

# class UserFollowView(View):

#     def get(self,request,*args,**kwargs):
#         #print(request,args,kwargs)
#         username = kwargs.get('username')
#         toggle_user = get_object_or_404(User,username__iexact=kwargs.get('username'))
#         #print(toggle_user)
#         if request.user.is_authenticated:
#             user_profile,created = Follow.objects.get_or_create(user=request.user)
#             if toggle_user in user_profile.following.all():
#                 user_profile.following.remove(toggle_user)
#             else:
#                 user_profile.following.add(toggle_user)
#         return redirect("user-following",username=username)

def userfollow(request,username):
    toggle_user = get_object_or_404(User,username__iexact=username)
    print(toggle_user)
    if request.user.is_authenticated and toggle_user != request.user :
        user_profile = Follow.objects.get(profile=request.user)
        print("User Profile ")
        print(user_profile)
        if toggle_user in user_profile.following.all():
            print("inside if ")
            user_profile.following.remove(toggle_user)
        else:
            print('inside else')
            user_profile.following.add(toggle_user)
    return redirect('user-following',username=request.user)


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        return render(request,'users/register.html',{'form':form})


def profile(request):
    form = UserProfileForm(instance=request.user.profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            print(profile)
            profile.user = request.user
            profile.save()
            return render(request,'users/edit_profile.html',{"form":form})
    return render(request,'users/edit_profile.html',{"form":form})