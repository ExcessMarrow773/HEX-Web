from django.shortcuts import render

# Create your views here.
def puzzles(request):
    context = {}
    return render(request, "encription/puzzles.html", context)

def create(request):
    context = {}
    return render(request, "encryption/create.html", context)

def viewer(request):
    context = {}
    return render(request, "encryption/viewer.html", context)