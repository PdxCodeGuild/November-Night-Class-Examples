from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(TimeStampedModel):
    body = models.CharField(max_length=512)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-created_at']

