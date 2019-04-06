from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Follow
from django.urls import reverse_lazy

class UserModelSerializers(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'profile_image_url',
            'url'
        ]

    def get_profile_image_url(self,obj):
        return obj.profile.image.url

    def get_url(self,obj):
        return reverse_lazy("user-detail",kwargs={"username":obj.username})

