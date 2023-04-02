from datetime import datetime, timedelta
from . import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from json import JSONEncoder, dumps

class SessionExpiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                delta = datetime.now() - last_activity
                if delta > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                    request.session.flush()
                    return HttpResponseRedirect(reverse('session-expired'))
            request.session['last_activity'] = dumps(datetime.now())
        response = self.get_response(request)
        return response
    