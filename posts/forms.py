from django import forms
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()
# Create your forms here


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']