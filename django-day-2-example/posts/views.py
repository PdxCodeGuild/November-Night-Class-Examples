from django.shortcuts import render, redirect

from posts.models import Post


def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})

def delete(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()

    return redirect('/')