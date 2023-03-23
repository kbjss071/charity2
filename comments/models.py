from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('charity.Post', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author.username} - {self.post.title}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])


