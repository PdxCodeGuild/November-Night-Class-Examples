from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Tweet

class TweetListView(ListView):
    model = Tweet

class TweetDetailView(DetailView):
    model = Tweet

class TweetCreateView(CreateView):
    model = Tweet
    fields = ['body']
    success_url = reverse_lazy('tweets:list')

class TweetUpdateView(UpdateView):
    model = Tweet
    fields = ['body']

class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy('tweets:list')