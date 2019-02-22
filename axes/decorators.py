from functools import wraps

from axes.handlers.proxy import AxesProxyHandler
from axes.utils import get_lockout_response


def axes_dispatch(func):
    def inner(request, *args, **kwargs):
        if AxesProxyHandler.is_allowed(request):
            return func(request, *args, **kwargs)

        return get_lockout_response(request)

    return inner


def axes_form_invalid(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        if AxesProxyHandler.is_allowed(self.request):
            return func(self, *args, **kwargs)

        return get_lockout_response(self.request)


    return inner
