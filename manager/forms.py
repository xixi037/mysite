from django import forms

from account.models import UserInfo


class UserInfoForm(forms.ModelForm):
    user = forms.CharField(max_length=10)
    class Meta:
        model = UserInfo
        exclude = ("phone","email")