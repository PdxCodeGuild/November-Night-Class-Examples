from django.urls import path

from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView,
)

app_name = 'tweets'
urlpatterns = [
    path('', TweetListView.as_view(), name='list'),
    path('create', TweetCreateView.as_view(), name='create'),
    path('<int:pk>', TweetDetailView.as_view(), name='detail'),
    path('update/<int:pk>', TweetUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TweetDeleteView.as_view(), name='delete'),
]