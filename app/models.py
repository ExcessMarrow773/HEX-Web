from django.db import models

# Create your models here.

class Post(models.Model):
    author_id = models.IntegerField(default=0)
    title = models.TextField()
    