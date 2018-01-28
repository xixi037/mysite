from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User,unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    classID = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True, default='')
    email = models.CharField(max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return "user:{}".format(self.user.username)

class UserProInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    pro_name = models.CharField(max_length=255, blank=True, null=True, default='')
    tutor = models.CharField(max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return "user:{}".format(self.user.username)