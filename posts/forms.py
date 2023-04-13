from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("title", "description", "target_amount")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args,**kwargs)