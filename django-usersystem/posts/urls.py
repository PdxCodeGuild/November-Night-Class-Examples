from django.urls import path

from posts import views

app_name = 'posts'
urlpatterns = [
    path('edit/<str:pk>', views.edit, name='edit'),
]