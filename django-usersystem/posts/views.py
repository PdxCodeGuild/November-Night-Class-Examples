from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from posts.models import Post
from posts.forms import PostForm
from posts.decorators import user_is_owner

@login_required
@user_is_owner(Post)
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit.html', {'form': form})