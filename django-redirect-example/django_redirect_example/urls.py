from django.contrib import admin
from django.urls import path

from django.http import HttpResponseRedirect

def redirect_to_google(request):
    location = request.GET.get('url', '//google.com')

    return HttpResponseRedirect(location)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_google),
]
