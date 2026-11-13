from django.db import models
from accounts.models import Profile

puzzle_types_choices = [
    (1, "Encryption"),
    (2, "Subsitution"),
    (3, "Enigma")
]

# Create your models here.
class Puzzle(models.Model):

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices=puzzle_types_choices)
    input = models.TextField()

    created_on = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
