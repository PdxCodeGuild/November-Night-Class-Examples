from django.db import models
from django.urls import reverse

class Tweet(models.Model):
    body = models.CharField(max_length=280)

    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('tweets:detail', kwargs={'pk': self.pk})