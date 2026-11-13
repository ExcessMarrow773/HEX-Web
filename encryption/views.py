from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model

from encryption.forms import CreatePuzzle
from encryption.models import Puzzle

User = get_user_model()
# Create your views here.
def puzzles(request):
    context = {}
    return render(request, "encription/puzzles.html", context)

def create(request):
    if request.method == "POST":
        form = CreatePuzzle(request.POST)
        if form.is_valid():
            puzzle = Puzzle(
                # created_by=get_object_or_404(User, pk=request.user.pk).profile,
                name=form.cleaned_data["name"],
                type=form.cleaned_data["type"]
            )
            puzzle.save()
            return redirect("app:index")
    else:
        form = CreatePuzzle()

    context = {
        'form': form
    }
    return render(request, "encryption/create.html", context)

def viewer(request):
    context = {}
    return render(request, "encryption/viewer.html", context)