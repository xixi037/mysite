from django import forms
from .models import UserInfo, UserProInfo, ProApply, ProMiddle, ProConclude


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

class ProApplyForm(forms.ModelForm):
    Pro_Way = (
        ('从开放实验项目库中选取','从开放实验项目库中选取'),
        ('项目组成员自主命题','项目组成员自主命题'),
        ('其它','其它')
    )
    pro_way = forms.CharField(widget=forms.Select(choices=Pro_Way))
    class Meta:
        model = ProApply
        exclude = ('pro_id',)

class ProMiddleForm(forms.ModelForm):
    class Meta:
        model = ProMiddle
        exclude = ('pro_id',)


class ProConcludeForm(forms.ModelForm):
    Pro_Status = (
        ('提前', '提前'),
        ('按时', '按时'),
        ('延期', '延期')
    )
    pro_status = forms.CharField(widget=forms.Select(choices=Pro_Status))
    class Meta:
        model = ProConclude
        exclude = ('pro_id',)