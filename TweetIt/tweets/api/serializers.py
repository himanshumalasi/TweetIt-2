from rest_framework import serializers
from tweets.models import Tweet
from users.api.serializers import UserModelSerializers

class ParentTweetModelSerializer(serializers.ModelSerializer): 
    user = UserModelSerializers(read_only=True)
    date_posted = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'date_posted',
        ]
    

    def get_date_posted(self,obj):
        return obj.date_posted.strftime("%b %d, %Y at %I:%M %p")

class TweetModelSerializer(serializers.ModelSerializer): 
    user = UserModelSerializers(read_only=True)
    date_posted = serializers.SerializerMethodField()
    parent = ParentTweetModelSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    #did_like = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'date_posted',
            'parent',
            'likes',
            'is_liked',
        ]

    def get_is_liked(self,obj):
        request = self.context.get('request')
        try:
            if request.user.is_authenticated:
                if request.user in obj.likes.all():
                    return True
                else:
                    return False
        except:
            return False

    # def get_request_user(self,obj):
    #     user = self.context.get("request").user.username
    #     return user

    # def get_did_like(self,obj):
    #     request = self.context.get("request")
    #     user = request.user
    #     if user.is_authenticated:
    #         if user in obj.liked.all():
    #             return True
    #     return False

    def get_likes(self,obj):
        return obj.liked.all().count()

    def get_date_posted(self,obj):
        return obj.date_posted.strftime("%b %d, %Y at %I:%M %p")



    