from django.urls import path

from .views import groceries

app_name = 'groceries'
urlpatterns = [
    path('', groceries, name='list'),
]