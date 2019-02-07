from django.urls import path

from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('preview/<str:code>', views.preview, name='preview'),
    path('<str:code>', views.redirect_url, name='redirect')
]