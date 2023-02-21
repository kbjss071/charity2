from rest_framework import serializers
from back.models import UserProfile, Post, Comment

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'