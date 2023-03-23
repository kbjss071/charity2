from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("title", "text" "donation_goal")
        model = models.Post
