from django import forms
from .models import UserInfo, UserProInfo


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("phone","email")


class UserProInfoForm(forms.ModelForm):
    class Meta:
        model = UserProInfo
        fields = ("tutor", "pro_name")