from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
# from account.models import Users
from manager.models import Members

def manager_home(request):
    return render(request, "manager/home.html")