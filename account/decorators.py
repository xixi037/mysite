from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.urls import reverse

from account.models import UserProInfo, UserInfo


def home_required(func):

    def wrapper(*args,**kwargs):
        for a in args:
            if isinstance(a,WSGIRequest):
                user = a.user
                user_obj = User.objects.get(username=user.username)
                if not UserProInfo.objects.filter(user=user_obj):
                    # return HttpResponseRedirect('/account/index')
                    return HttpResponseRedirect(reverse('account:account_index'))

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
                    # return HttpResponseRedirect('/account/home')
                    return HttpResponseRedirect(reverse('account:account_home'))

        return func(*args,**kwargs)
    return wrapper

def userinfo_required(func):

    def wrapper(*args,**kwargs):
        for a in args:
            if isinstance(a,WSGIRequest):
                user = a.user
                user_obj = User.objects.get(username=user.username)
                if UserInfo.objects.filter(user=user_obj):
                    userinfo = UserInfo.objects.get(user=user_obj)
                    if userinfo.phone.strip() == "":
                        # return HttpResponseRedirect('/account/index/edit-my-information/')
                        return HttpResponseRedirect(reverse('account:index_edit_my_information'))

        return func(*args,**kwargs)
    return wrapper



