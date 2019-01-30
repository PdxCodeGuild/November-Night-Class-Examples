from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    posts_json = []

    for post in posts:
        posts_json.append({
            'title': post.title,
            'body': post.body
        })

    return JsonResponse(posts_json, safe=False)


def create(request):
    Post.objects.create(title="Hello", body="Yeah!")