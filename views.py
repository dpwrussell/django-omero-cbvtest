from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from omeroweb.webclient.decorators import login_required, render_response

class CBVTestView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(CBVTestView, self).dispatch(*args, **kwargs)