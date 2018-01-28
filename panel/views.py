from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
# from account.models import Users
from panel.models import ProInfo, Members


def panel_home(request):
    return render(request,"panel/home.html")

# def panel_mypro(request):
#     username = request.COOKIES.get('username')
#     info = []
#     if ProInfo.objects.filter(leader_id=username):
#         leader = Users.objects.get(username=username)
#         pro = ProInfo.objects.filter(leader_id=username)
#         for i in pro:
#             info1 = model_to_dict(i)
#             mem_info = Members.objects.filter(pro_id=i.id)
#             memlist = []
#             for i in mem_info:
#                 memlist.append(i.stu_id)
#             memlist = '/'.join(memlist)
#             info1["pro_mems"] = memlist
#             info1["name"] = leader.name
#             info.append(info1)
#     if Members.objects.filter(stu_id=username):
#         print('')
#         pro = Members.objects.filter(stu_id=username)
#         for i in pro:
#             id = i.pro_id
#             pro = ProInfo.objects.filter(id=id)
#             for i in pro:
#                 info2 = model_to_dict(i)
#                 leader = Users.objects.get(username=i.leader_id)
#                 mem_info = Members.objects.filter(pro_id=i.id)
#                 memlist = []
#                 for k in mem_info:
#                     memlist.append(k.stu_id)
#                 memlist = '/'.join(memlist)
#                 info2["pro_mems"] = memlist
#                 info2["name"] = leader.name
#                 info.append(info2)
#     return render(request, 'panel/mypro.html', {'infolist': info})