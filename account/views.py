from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from account.models import UserInfo, UserProInfo
from .forms import LoginForm, UserInfoForm, UserProInfoForm


# Create your views here.


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("账号或密码错误！")
        else:
            return HttpResponse("无效登录！")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def password_change(request):
    return render(request, 'account/password_change.html')

@login_required(login_url='/account/login/')
def user_info(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,"account/userinfo.html",{"user":user,"userinfo":userinfo})

@login_required(login_url='/account/login/')
def user_info_edit(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)

    if request.method == "POST":
        userinfo_form = UserInfoForm(request.POST)

        if userinfo_form.is_valid():
            userinfo_cd = userinfo_form.cleaned_data
            userinfo.phone = userinfo_cd['phone']
            userinfo.email = userinfo_cd['email']
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        userinfo_form = UserInfoForm(initial={"phone":userinfo.phone,"email":userinfo.email})
        return render(request,"account/userinfo_edit.html",{"user":user,"userinfo":userinfo,"userinfo_form":userinfo_form})

@login_required(login_url='/account/login/')
def user_pro_info(request):
    user = User.objects.get(username=request.user.username)
    userproinfo = UserProInfo.objects.get(user=user)
    return render(request, "account/proinfo.html", {"user": user, "userproinfo": userproinfo})

@login_required(login_url='/account/login/')
def user_pro_info_edit(request):
    user = User.objects.get(username=request.user.username)
    userproinfo = UserProInfo.objects.get(user=user)

    if request.method == "POST":
        userproinfo_form = UserProInfoForm(request.POST)

        if userproinfo_form.is_valid():
            userproinfo_cd = userproinfo_form.cleaned_data
            userproinfo.tutor = userproinfo_cd['tutor']
            userproinfo.pro_name = userproinfo_cd['pro_name']
            userproinfo.save()
        return HttpResponseRedirect('/account/my-pro-information/')
    else:
        userproinfo_form = UserProInfoForm(initial={"tutor":userproinfo.tutor,"pro_name":userproinfo.pro_name})
        return render(request,"account/proinfo_edit.html",{"user":user,"userproinfo_form":userproinfo_form})