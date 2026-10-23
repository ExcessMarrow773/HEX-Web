from django.db import models
from accounts.models import Profile

# Create your models here.

class Link(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name