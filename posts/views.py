from django.shortcuts import render

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
