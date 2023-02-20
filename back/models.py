from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blanks = True)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    context = models.CharField()
    create_at = models.DateTimeField(auto_now_add=True)
    post_pic = models.ImageField(upload_to='post_pics', blanks=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    context = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.context