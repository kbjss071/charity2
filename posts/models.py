from django.db import models
from django.conf import settings
from django.urls import reverse
# from comments.models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_names="posts", on_delete=models.CASCADE)
    text = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    name = models.TextField()
    members = models.ManyToManyField(User, through="donateMember")
    amount = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.subject
    
    def save(self, *args, **kwargs):
        super.save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "slug": self.slug
            }
        )
    
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "subject"]