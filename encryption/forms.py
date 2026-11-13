from django import forms
from django.contrib.auth import get_user_model

from encryption.models import Puzzle

User = get_user_model()
# Create your forms here


class CreatePuzzle(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ['name', 'type', 'input']