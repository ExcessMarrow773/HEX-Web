from django.shortcuts import render, get_object_or_404

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from posts.forms import CreatePost
from posts.models import Post

from accounts.models import CustomUser

User = get_user_model()
# Create your views here.

# @login_required
def makePost(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post = Post(
                author=get_object_or_404(User, pk=request.user.pk),
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"]
            )
            post.save()
            return redirect('app:index')
    else:
        form = CreatePost()
    
    context = {
        'form': form
    }
    return render(request, 'posts/makePost.html', context)
