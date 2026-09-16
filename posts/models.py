from django.db import models
from django.urls import reverse

from accounts.models import Profile
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('posts:viewPost', kwargs={'pk': self.pk})


    def __str__(self) -> str:
        return f'{self.author.account().name()}: {self.title}'