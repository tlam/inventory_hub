from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

class RequireLoginMiddleware(object):
    def __init__(self):
        self.path_exceptions = [
            reverse('admin:index'),
            reverse('hub-users:login'),
        ]

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated():
            return None

        for url in self.path_exceptions:
            if request.path.startswith(url):
                return None

        return redirect('hub-users:login')
