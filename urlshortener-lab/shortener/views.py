from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .models import ShortURL


def index(request):
    if request.method == 'POST':
        # From the HTML form
        form_url = request.POST['url']

        # New ShortURL
        url = ShortURL()
        url.url = form_url
        url.generate_code()
        url.save()
        return redirect('shortener:preview', code=url.code)

    return render(request, 'shortener/index.html')


def preview(request, code):
    url = get_object_or_404(ShortURL, code=code)
    return render(request, 'shortener/preview.html', {'url': url})


def redirect_url(request, code):
    url = get_object_or_404(ShortURL, code=code)
    return HttpResponseRedirect(url.url)