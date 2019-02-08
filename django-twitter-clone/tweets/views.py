from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Tweet

# C
class TweetCreateView(CreateView):
    model = Tweet
    fields = ['body']
    success_url = reverse_lazy('tweets:list')

# R
class TweetDetailView(DetailView):
    model = Tweet

# U
class TweetUpdateView(UpdateView):
    model = Tweet
    fields = ['body']

# D
class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy('tweets:list')

# L 
class TweetListView(ListView):
    model = Tweet