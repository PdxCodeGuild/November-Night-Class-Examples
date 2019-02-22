from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from posts.models import Post

class user_is_owner:
    def __init__(self, model):
        self.model = model

    def __call__(self, function):
        def wrap(request, *args, **kwargs):
            model = self.model.objects.get(pk=kwargs['pk'])
            if model.user == request.user:
                return function(request, *args, **kwargs)
            else:
                return redirect('/')

        wrap.__doc__ = function.__doc__
        wrap.__name__ = function.__name__
        return wrap
