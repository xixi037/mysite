from django.contrib import admin
from .models import UserInfo, UserProInfo, ProApply, ProMiddle, ProConclude


# Register your models here.

class UsersInfoAdmin(admin.ModelAdmin):
    list_display = ('user','name','major')
    list_filter = ("classID",)

admin.site.register(UserInfo,UsersInfoAdmin)

class UserProInfoAdmin(admin.ModelAdmin):
    list_display = ('user','tutor','pro_name')
    list_filter = ('tutor',)

admin.site.register(UserProInfo,UserProInfoAdmin)

class ProApplyAdmin(admin.ModelAdmin):
    list_display = ('pro_id','status')
    list_filter = ('status',)

admin.site.register(ProApply,ProApplyAdmin)

class ProMiddleAdmin(admin.ModelAdmin):
    list_display = ('pro_id','status')
    list_filter = ('status',)

admin.site.register(ProMiddle,ProMiddleAdmin)

class ProConcludeAdmin(admin.ModelAdmin):
    list_display = ('pro_id','status')
    list_filter = ('status',)

admin.site.register(ProConclude,ProConcludeAdmin)
