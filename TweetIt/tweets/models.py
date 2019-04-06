from django.db import models
from django.contrib.auth.models import User

class TweetManager(models.Manager):

	def retweet(self,user,parent_obj,*args,**kwargs):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else:
			og_parent = parent_obj
		qs = self.get_queryset().filter(user=user,parent=og_parent)
		if qs.exists():
			return None

		obj = self.model(
			parent=og_parent,
			user=user,
			content = og_parent.content,
		)
		obj.save()
		return obj
	
	def like_toggle(self,user,tweet_obj):
		if user in tweet_obj.liked.all():
			is_liked = False
			tweet_obj.liked.remove(user)
		else:
			is_liked = True
			tweet_obj.liked.add(user)
		return is_liked


class Tweet(models.Model):
	parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.CharField(max_length=140)
	liked = models.ManyToManyField(User,blank=True,related_name='liked')
	date_posted = models.DateTimeField(auto_now_add=True)
	timestamp = models.DateTimeField(auto_now = True)
	
	objects = TweetManager()

	def  __str__(self):
		return self.content
	class Meta:
		ordering = ['-date_posted']