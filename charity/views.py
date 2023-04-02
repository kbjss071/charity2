from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from . import settings
from datetime import datetime

class LoginPage(TemplateView):
    template_name = 'after_login.html'

class LogoutPage(TemplateView):
    template_name = 'after_logout.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)
    
def session_expired(request):
    return render(request, 'session_expired.html')
