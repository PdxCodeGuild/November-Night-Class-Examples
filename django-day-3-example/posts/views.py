from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post, Comment
from posts.serializers import PostSerializer

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def retrieve(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/retrieve.html', {'post': post})

def create_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment = Comment()
        comment.body = request.POST['body']
        comment.post = post
        comment.save()
    
    return redirect('posts:retrieve', id=post.id)


@api_view(['GET'])
def api_posts(requests):
    posts = Post.objects.all()
    payload = PostSerializer(posts, many=True)

    return Response(data=payload.data)