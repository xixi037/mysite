from django.contrib import admin
from .models import UserInfo
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user','name','major')
    list_filter = ("classID",)

admin.site.register(UserInfo,UsersAdmin)
