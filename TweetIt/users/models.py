from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
    profile = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    following = models.ManyToManyField(User,related_name='followed_by',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.profile.username)
    
    def __str__(self):
        return str(self.following.all().count())

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    cover = models.ImageField(default='cover.jpg',upload_to='cover_pics')
    description = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"


