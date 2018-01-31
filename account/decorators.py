from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect

from account.models import UserProInfo


def home_required(func):

    def wrapper(*args,**kwargs):
        for a in args:
            if isinstance(a,WSGIRequest):
                user = a.user
                print(user.username)
                user_obj = User.objects.get(username=user.username)
                if not UserProInfo.objects.filter(user=user_obj):
                    return HttpResponseRedirect('/account/')

        return func(*args,**kwargs)
    return wrapper


def index_required(func):

    def wrapper(*args,**kwargs):
        for a in args:
            if isinstance(a,WSGIRequest):
                user = a.user
                print(user.username)
                user_obj = User.objects.get(username=user.username)
                if UserProInfo.objects.filter(user=user_obj):
                    return HttpResponseRedirect('/account/home')

        return func(*args,**kwargs)
    return wrapper

