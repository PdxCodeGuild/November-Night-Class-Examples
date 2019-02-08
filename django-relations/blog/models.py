from django.db import models
from django.contrib.auth.models import User
from markupfield.fields import MarkupField

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(TimeStampedModel):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(TimeStampedModel):
    title = models.CharField(max_length=128)
    body = MarkupField()

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')


class Comment(TimeStampedModel):
    body = models.CharField(max_length=512)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')