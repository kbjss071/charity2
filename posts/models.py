from django.db import models
from django.conf import settings
from django.urls import reverse
# from comments.models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_names="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    donors = models.ManyToManyField(User, through="donateMember")
    current_amount = models.DecimalField(max_digits=15, decimal_places=2)
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_donors_count(self):
        return self.donors.count()
    
    def get_donation_progress(self):
        return (self.current_amount/self.target_amount)*100

    # def get_absolute_url(self):
    #     return reverse(
    #         "posts:single",
    #         kwargs={
    #             "slug": self.slug
    #         }
    #     )
    
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "title"]