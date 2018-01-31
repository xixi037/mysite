import win32com.client
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# from account.models import Users
import math
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import os
from email.header import make_header

import pythoncom
import time

from account.models import UserInfo, UserProInfo, ProApply, ProMiddle, ProConclude
from manager.forms import UserInfoForm
from manager.models import Status


@permission_required('account.add_userproinfo',login_url="/account/login/")
def manager_home(request):
    return render(request, "manager/home.html")

@permission_required('account.add_userproinfo',login_url="/account/login/")
@csrf_exempt
def userlist(request):
    if request.method == "GET":
        userinfo = UserInfo.objects.all()
        userinfo_form = UserInfoForm()
        return render(request,'manager/userlist.html',{'userinfo':userinfo,'userinfo_form':userinfo_form})

    if request.method == "POST":
        user = request.POST['user']
        # row_password = 'szu'+str(user)[-6:]
        # print(row_password)
        # password = make_password(row_password)
        password = 'szu'+str(user)[-6:]
        print(password)
        name = request.POST['name']
        sex = request.POST['sex']
        classID = request.POST['classID']
        major = request.POST['major']
        institute = request.POST['institute']
        user_obj = User.objects.filter(username=user)
        if user_obj:
            pass
        else:
            user = User.objects.create_user(username=user, password=password)
            user.save()
        user_instance = User.objects.get(username=user)
        userinfo_obj = UserInfo.objects.filter(user=user_instance)
        if userinfo_obj:
            return HttpResponse('2')
        else:
            UserInfo.objects.create(user=user_instance, name=name, sex=sex, classID=classID, major=major,
                                    institute=institute)
            return HttpResponse('1')

@permission_required('account.add_userproinfo',login_url="/account/login/")
@require_POST
@csrf_exempt
def del_userlist(request):
    user = request.POST['user_id']
    try:
        user_obj = User.objects.get(username=user)
        if UserInfo.objects.filter(user=user_obj):
            userinfo_obj = UserInfo.objects.get(user=user_obj)

            if ProApply.objects.filter(pro_id=userinfo_obj):
                ProApply.objects.get(pro_id=userinfo_obj).delete()
            if ProMiddle.objects.filter(pro_id=userinfo_obj):
                ProMiddle.objects.get(pro_id=userinfo_obj).delete()
            if ProConclude.objects.filter(pro_id=userinfo_obj):
                ProConclude.objects.get(pro_id=userinfo_obj).delete()

            userinfo_obj.delete()
            user_obj.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@permission_required('account.add_userproinfo',login_url="/account/login/")
def apply_infolist(request):
    infolist = []
    prolist = ProApply.objects.filter(status=2)
    print(prolist)
    for i in prolist:
        print(i.pro_id_id)
        pro_id = i.pro_id_id
        records = UserProInfo.objects.filter(id=pro_id)
        for k in records:
            dict = model_to_dict(k)
            user = k.user
            userinfo = UserInfo.objects.filter(user=user)
            for j in userinfo:
                name = j.name
            dict['user'] = user
            dict['name'] = name
            infolist.append(dict)
    return render(request, 'manager/infolist_apply.html',{'infolist': infolist})

@permission_required('account.add_userproinfo',login_url="/account/login/")
def middle_infolist(request):
    infolist = []
    prolist = ProMiddle.objects.filter(status=2)
    print(prolist)
    for i in prolist:
        print(i.pro_id_id)
        pro_id = i.pro_id_id
        records = UserProInfo.objects.filter(id=pro_id)
        for k in records:
            dict = model_to_dict(k)
            user = k.user
            userinfo = UserInfo.objects.filter(user=user)
            for j in userinfo:
                name = j.name
            dict['user'] = user
            dict['name'] = name
            infolist.append(dict)
    return render(request, 'manager/infolist_middle.html',{'infolist': infolist})

@permission_required('account.add_userproinfo',login_url="/account/login/")
def conclude_infolist(request):
    infolist = []
    prolist = ProConclude.objects.filter(status=2)
    print(prolist)
    for i in prolist:
        print(i.pro_id_id)
        pro_id = i.pro_id_id
        records = UserProInfo.objects.filter(id=pro_id)
        for k in records:
            dict = model_to_dict(k)
            user = k.user
            userinfo = UserInfo.objects.filter(user=user)
            for j in userinfo:
                name = j.name
            dict['user'] = user
            dict['name'] = name
            infolist.append(dict)
    return render(request, 'manager/infolist_conclude.html',{'infolist': infolist})


@permission_required('account.add_userproinfo',login_url="/account/login/")
def others_infolist(request):
    base_path = os.getcwd()
    file = 'other'
    file_dir = os.path.join(base_path, file)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    filelist = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filelist.append(file)
    return render(request, 'manager/infolist_files.html', {'infolist': filelist})


def tolist(source):
    list = []
    for item in source:
        list.append(item.get('value'))
    return list

def todict(source):
    target = {}
    for item in source:
        target.__setitem__(item.get('name'), item.get('value'))
    return target

def write_to_apply(request):
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        print(choicelist)
        choicelist = tolist(choicelist)
        pathlist = []
        for user in choicelist:
            user_obj = User.objects.get(username=user)
            user_info = UserInfo.objects.get(user=user_obj)
            pro_info = UserProInfo.objects.get(user=user_obj)
            if ProApply.objects.filter(pro_id=pro_info.id):
                info = ProApply.objects.get(pro_id=pro_info.id)


                filename = '申请报告模板.doc'
                open_path = os.getcwd() + os.sep + 'models'
                save_path = os.getcwd() + os.sep + 'apply'
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                file = os.path.join(open_path, filename)

                pro_name = pro_info.pro_name
                tutor_name = pro_info.tutor

                pro_leader = user_info.name
                leader_sex = user_info.sex
                leader_major = user_info.major
                leader_institute = user_info.institute
                leader_phone = user_info.phone
                leader_email = user_info.email

                savename = '申请报告_' + tutor_name + '_' + pro_leader + '_' + pro_name + '.doc'

                savepath = os.path.join(save_path, savename)
                if os.path.exists(savepath) is False:

                    pythoncom.CoInitialize()
                    try:
                        app = win32com.client.Dispatch('word.Application')
                        doc = app.Documents.Open(file)
                        print('打开的是word')
                    except:
                        app = win32com.client.Dispatch('kwps.Application')
                        doc = app.Documents.Open(file)
                        print('打开的是wps')


                    # 第一张表填写位置
                    t1 = doc.Tables[0]
                    pro_name_pos = t1.Cell(2, 2)
                    pro_leader_pos = t1.Cell(3, 2)
                    leader_phone_pos = t1.Cell(4, 2)
                    leader_email_pos = t1.Cell(5, 2)
                    apply_time_pos = t1.Cell(6, 2)

                    pro_name_pos.Range.Text = pro_name
                    pro_leader_pos.Range.Text = pro_leader
                    leader_phone_pos.Range.Text = leader_phone
                    leader_email_pos.Range.Text = leader_email
                    apply_time_pos.Range.Text = info.fillin_time

                    t2 = doc.Tables[1]
                    pro_name1_pos = t2.Cell(1, 2)
                    pro_way_pos = t2.Cell(2, 2)
                    # search_area_pos = t2.Cell(3, 4)
                    pro_leader1_pos = t2.Cell(4, 2)
                    leader_sex_pos = t2.Cell(4, 4)
                    leader_id_pos = t2.Cell(4, 6)
                    leader_major_pos = t2.Cell(5, 2)
                    leader_institute_pos = t2.Cell(5, 4)
                    tutor_id_pos = t2.Cell(6, 2)
                    tutor_area_pos = t2.Cell(6, 4)
                    tutor_phone_pos = t2.Cell(7, 2)
                    tutor_email_pos = t2.Cell(7, 4)

                    pro_name1_pos.Range.Text = pro_name
                    pro_way_pos.Range.Text = info.pro_way
                    # search_area_pos.Range.Text = info.search_area
                    pro_leader1_pos.Range.Text = pro_leader
                    leader_sex_pos.Range.Text = leader_sex
                    leader_id_pos.Range.Text = user
                    leader_major_pos.Range.Text = leader_major
                    leader_institute_pos.Range.Text = leader_institute
                    tutor_id_pos.Range.Text = tutor_name
                    tutor_area_pos.Range.Text = info.tutor_area
                    tutor_phone_pos.Range.Text = info.tutor_phone
                    tutor_email_pos.Range.Text = info.tutor_email

                    pro_leader2_pos = t2.Cell(9, 2)
                    leader_sex1_pos = t2.Cell(9, 3)
                    leader_id1_pos = t2.Cell(9, 4)
                    leader_grade_pos = t2.Cell(9, 5)
                    leader_area_pos = t2.Cell(9, 6)
                    leader_job_pos = t2.Cell(9, 7)
                    leader_institute1_pos = t2.Cell(9, 8)
                    mem1_name_pos = t2.Cell(10, 2)
                    mem1_sex_pos = t2.Cell(10, 3)
                    mem1_stuID_pos = t2.Cell(10, 4)
                    mem1_grade_pos = t2.Cell(10, 5)
                    mem1_area_pos = t2.Cell(10, 6)
                    mem1_job_pos = t2.Cell(10, 7)
                    mem1_institute_pos = t2.Cell(10, 8)
                    mem2_name_pos = t2.Cell(11, 2)
                    mem2_sex_pos = t2.Cell(11, 3)
                    mem2_stuID_pos = t2.Cell(11, 4)
                    mem2_grade_pos = t2.Cell(11, 5)
                    mem2_area_pos = t2.Cell(11, 6)
                    mem2_job_pos = t2.Cell(11, 7)
                    mem2_institute_pos = t2.Cell(11, 8)
                    mem3_name_pos = t2.Cell(12, 2)
                    mem3_sex_pos = t2.Cell(12, 3)
                    mem3_stuID_pos = t2.Cell(12, 4)
                    mem3_grade_pos = t2.Cell(12, 5)
                    mem3_area_pos = t2.Cell(12, 6)
                    mem3_job_pos = t2.Cell(12, 7)
                    mem3_institute_pos = t2.Cell(12, 8)

                    pro_leader2_pos.Range.Text = pro_leader
                    leader_sex1_pos.Range.Text = leader_sex
                    leader_id1_pos.Range.Text = user
                    leader_grade_pos.Range.Text = pro_leader
                    leader_area_pos.Range.Text = leader_sex
                    leader_job_pos.Range.Text = info.leader_job
                    leader_institute1_pos.Range.Text = leader_institute
                    mem1_name_pos.Range.Text = info.mem1_name
                    mem1_sex_pos.Range.Text = info.mem1_sex
                    mem1_stuID_pos.Range.Text = info.mem1_stuID
                    mem1_grade_pos.Range.Text = info.mem1_grade
                    mem1_area_pos.Range.Text = info.mem1_area
                    mem1_job_pos.Range.Text = info.mem1_job
                    mem1_institute_pos.Range.Text = info.mem1_institute
                    mem2_name_pos.Range.Text = info.mem2_name
                    mem2_sex_pos.Range.Text = info.mem2_sex
                    mem2_stuID_pos.Range.Text = info.mem2_stuID
                    mem2_grade_pos.Range.Text = info.mem2_grade
                    mem2_area_pos.Range.Text = info.mem2_area
                    mem2_job_pos.Range.Text = info.mem2_job
                    mem2_institute_pos.Range.Text = info.mem2_institute
                    mem3_name_pos.Range.Text = info.mem3_name
                    mem3_sex_pos.Range.Text = info.mem3_sex
                    mem3_stuID_pos.Range.Text = info.mem3_stuID
                    mem3_grade_pos.Range.Text = info.mem3_grade
                    mem3_area_pos.Range.Text = info.mem3_area
                    mem3_job_pos.Range.Text = info.mem3_job
                    mem3_institute_pos.Range.Text = info.mem3_institute

                    pro_reason_pos = t2.Cell(13, 1)
                    pro_content_pos = t2.Cell(14, 1)
                    pro_innovation_pos = t2.Cell(15, 1)
                    pro_source_pos = t2.Cell(16, 1)

                    reason_title = str(pro_reason_pos).replace('\r', '')
                    content_title = str(pro_content_pos).replace('\r', '')
                    innovation_title = str(pro_innovation_pos).replace('\r', '')
                    source_title = str(pro_source_pos).replace('\r', '')

                    if info.pro_reason.strip() != '':
                        pro_reason_pos.Range.Text = reason_title + '\n' + info.pro_reason
                    if info.pro_content.strip() != '':
                        pro_content_pos.Range.Text = content_title + '\n' + info.pro_content
                    if info.pro_innovation.strip() != '':
                        pro_innovation_pos.Range.Text = innovation_title + '\n' + info.pro_innovation
                    if info.pro_source.strip() != '':
                        pro_source_pos.Range.Text = source_title + '\n' + info.pro_source

                    time1_pos = t2.Cell(19, 1)
                    content1_pos = t2.Cell(19, 2)
                    leader1_pos = t2.Cell(19, 3)
                    time2_pos = t2.Cell(20, 1)
                    content2_pos = t2.Cell(20, 2)
                    leader2_pos = t2.Cell(20, 3)
                    time3_pos = t2.Cell(21, 1)
                    content3_pos = t2.Cell(21, 2)
                    leader3_pos = t2.Cell(21, 3)
                    time4_pos = t2.Cell(22, 1)
                    content4_pos = t2.Cell(22, 2)
                    leader4_pos = t2.Cell(22, 3)
                    time5_pos = t2.Cell(23, 1)
                    content5_pos = t2.Cell(23, 2)
                    leader5_pos = t2.Cell(23, 3)
                    time6_pos = t2.Cell(24, 1)
                    content6_pos = t2.Cell(24, 2)
                    leader6_pos = t2.Cell(24, 3)
                    time7_pos = t2.Cell(25, 1)
                    content7_pos = t2.Cell(25, 2)
                    leader7_pos = t2.Cell(25, 3)

                    time1_pos.Range.Text = info.time1
                    content1_pos.Range.Text = info.content1
                    leader1_pos.Range.Text = info.leader1
                    time2_pos.Range.Text = info.time2
                    content2_pos.Range.Text = info.content2
                    leader2_pos.Range.Text = info.leader2
                    time3_pos.Range.Text = info.time3
                    content3_pos.Range.Text = info.content3
                    leader3_pos.Range.Text = info.leader3
                    time4_pos.Range.Text = info.time4
                    content4_pos.Range.Text = info.content4
                    leader4_pos.Range.Text = info.leader4
                    time5_pos.Range.Text = info.time5
                    content5_pos.Range.Text = info.content5
                    leader5_pos.Range.Text = info.leader5
                    time6_pos.Range.Text = info.time6
                    content6_pos.Range.Text = info.content6
                    leader6_pos.Range.Text = info.leader6
                    time7_pos.Range.Text = info.time7
                    content7_pos.Range.Text = info.content7
                    leader7_pos.Range.Text = info.leader7

                    pro_achievement_pos = t2.Cell(28, 2)
                    pro_endtime_pos = t2.Cell(28, 3)
                    pro_form_pos = t2.Cell(28, 4)
                    pro_participant_pos = t2.Cell(28, 5)


                    pro_achievement_pos.Range.Text = info.pro_achievement
                    pro_endtime_pos.Range.Text = info.pro_endtime
                    pro_form_pos.Range.Text = info.pro_form
                    pro_participant_pos.Range.Text = info.pro_participant

                    t3 = doc.Tables[2]
                    budget_equip_money_pos = t3.Cell(3, 2)
                    budget_equip_reason_pos = t3.Cell(3, 3)
                    budget_material_money_pos = t3.Cell(4, 2)
                    budget_material_reason_pos = t3.Cell(4, 3)
                    budget_meeting_money_pos = t3.Cell(5, 2)
                    budget_meeting_reason_pos = t3.Cell(5, 3)
                    budget_apply_money_pos = t3.Cell(6, 2)
                    budget_apply_reason_pos = t3.Cell(6, 3)
                    budget_books_money_pos = t3.Cell(7, 2)
                    budget_books_reason_pos = t3.Cell(7, 3)
                    budget_trans_money_pos = t3.Cell(8, 2)
                    budget_trans_reason_pos = t3.Cell(8, 3)
                    budget_service_money_pos = t3.Cell(9, 2)
                    budget_service_reason_pos = t3.Cell(9, 3)
                    budget_other_money_pos = t3.Cell(10, 2)
                    budget_other_reason_pos = t3.Cell(10, 3)
                    budget_total_money_pos = t3.Cell(11, 2)

                    budget_equip_money_pos.Range.Text = info.budget_equip_money
                    budget_equip_reason_pos.Range.Text = info.budget_equip_reason
                    budget_material_money_pos.Range.Text = info.budget_material_money
                    budget_material_reason_pos.Range.Text = info.budget_material_reason
                    budget_meeting_money_pos.Range.Text = info.budget_meeting_money
                    budget_meeting_reason_pos.Range.Text = info.budget_meeting_reason
                    budget_apply_money_pos.Range.Text = info.budget_apply_money
                    budget_apply_reason_pos.Range.Text = info.budget_apply_reason
                    budget_books_money_pos.Range.Text = info.budget_books_money
                    budget_books_reason_pos.Range.Text = info.budget_books_reason
                    budget_trans_money_pos.Range.Text = info.budget_trans_money
                    budget_trans_reason_pos.Range.Text = info.budget_trans_reason
                    budget_service_money_pos.Range.Text = info.budget_service_money
                    budget_service_reason_pos.Range.Text = info.budget_service_reason
                    budget_other_money_pos.Range.Text = info.budget_other_money
                    budget_other_reason_pos.Range.Text = info.budget_other_reason
                    budget_total_money_pos.Range.Text = info.budget_total_money

                    doc.SaveAs(savepath)
                    doc.Close()
                    app.Quit()
                    print('保存完毕')
                    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                    ProApply.objects.filter(pro_id=pro_info.id).update(export_time=date)
                print(savepath.encode('utf-8'))
                pathlist.append(savepath)
        print(pathlist)
        pathdic = {"path":pathlist}
        print('路径dic为：')
        print(pathdic)
        return JsonResponse(pathdic)
    return 'error'

def write_to_middle(request):
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        print(choicelist)
        choicelist = tolist(choicelist)
        pathlist = []
        for user in choicelist:
            user_obj = User.objects.get(username=user)
            user_info = UserInfo.objects.get(user=user_obj)
            pro_info = UserProInfo.objects.get(user=user_obj)
            if ProMiddle.objects.filter(pro_id=pro_info.id):
                info = ProMiddle.objects.get(pro_id=pro_info.id)


                filename = '中期报告模板.doc'
                open_path = os.getcwd() + os.sep + 'models'
                save_path = os.getcwd() + os.sep + 'middle'
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                file = os.path.join(open_path, filename)
                print(file)


                pro_name = pro_info.pro_name
                tutor_name = pro_info.tutor


                pro_leader = user_info.name

                savename = '中期报告_' + tutor_name + '_' + pro_leader + '_' + pro_name + '.doc'

                savepath = os.path.join(save_path, savename)
                if os.path.exists(savepath) is False:

                    pythoncom.CoInitialize()
                    try:
                        app = win32com.client.Dispatch('word.Application')
                        doc = app.Documents.Open(file)
                        print('打开的是word')
                    except:
                        app = win32com.client.Dispatch('kwps.Application')
                        doc = app.Documents.Open(file)
                        print('打开的是wps')


                    # 第一张表填写位置
                    t1 = doc.Tables[0]
                    pro_num_pos = t1.Cell(1, 2)
                    pro_name_pos = t1.Cell(1, 4)
                    pro_leader_pos = t1.Cell(2, 2)
                    leader_stuID_pos = t1.Cell(2, 4)
                    leader_phone_pos = t1.Cell(2, 6)
                    pro_mems_pos = t1.Cell(3,2)
                    tutor_name_pos = t1.Cell(4, 2)
                    pro_period_pos = t1.Cell(5,2)
                    pro_endtime_pos = t1.Cell(5,4)
                    pro_schedule_pos = t1.Cell(6, 1)
                    pro_source_pos = t1.Cell(7, 1)
                    pro_money_pos = t1.Cell(8, 1)
                    pro_difficulties_pos = t1.Cell(9, 1)
                    pro_advice_pos = t1.Cell(10,1)
                    pro_change_pos = t1.Cell(11, 1)
                    pro_plan_pos = t1.Cell(12, 1)
                    pro_harvest_pos = t1.Cell(13, 1)

                    pro_num_pos.Range.Text = info.pro_num
                    leader_stuID_pos.Range.Text = info.leader_id
                    pro_mems_pos.Range.Text = info.pro_mems
                    pro_period_pos.Range.Text = info.pro_stime + '至' + info.pro_etime
                    pro_endtime_pos.Range.Text = info.pro_endtime

                    schedule_title = str(pro_schedule_pos).replace('\r', '')
                    source_title = str(pro_source_pos).replace('\r', '')
                    money_title = str(pro_money_pos).replace('\r', '')
                    difficulties_title = str(pro_difficulties_pos).replace('\r', '')
                    advice_title = str(pro_advice_pos).replace('\r', '')
                    change_title = str(pro_change_pos).replace('\r', '')
                    plan_title = str(pro_plan_pos).replace('\r', '')
                    harvest_title = str(pro_harvest_pos).replace('\r', '')
                    if info.pro_schedule.strip() != '':
                        pro_schedule_pos.Range.Text = schedule_title + '\n' + info.pro_schedule
                    if info.pro_source.strip() != '':
                        pro_source_pos.Range.Text = source_title + '\n' + info.pro_source
                    if info.pro_money.strip() != '':
                        pro_money_pos.Range.Text = money_title + '\n' + info.pro_money
                    if info.pro_difficulties.strip() != '':
                        pro_difficulties_pos.Range.Text = difficulties_title + '\n' + info.pro_difficulties
                    if info.pro_advice.strip() != '':
                        pro_advice_pos.Range.Text = advice_title + '\n' + info.pro_advice
                    if info.pro_change.strip() != '':
                        pro_change_pos.Range.Text = change_title + '\n' + info.pro_change
                    if info.pro_plan.strip() != '':
                        pro_plan_pos.Range.Text = plan_title + '\n' + info.pro_plan
                    if info.pro_harvest.strip() != '':
                        pro_harvest_pos.Range.Text = harvest_title + '\n' + info.pro_harvest

                    for info in pro_info:
                        pro_name_pos.Range.Text = info.pro_name
                        tutor_name_pos.Range.Text = info.tutor_id
                    for info in user_info:
                        pro_leader_pos.Range.Text = info.name
                        leader_phone_pos.Range.Text = info.phone


                    doc.SaveAs(savepath)
                    doc.Close()
                    app.Quit()
                    print('保存完毕')
                    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                    ProMiddle.objects.get(pro_id=pro_info.id).update(export_time=date)
                print(savepath.encode('utf-8'))
                pathlist.append(savepath)
        print(pathlist)
        pathdic = {"path":pathlist}
        print('路径dic为：')
        print(pathdic)
        return JsonResponse(pathdic)
    return 'error'

def write_to_conclude(request):
    print('写结题报告啦')
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        print(choicelist)
        choicelist = tolist(choicelist)
        pathlist = []
        for user in choicelist:
            user_obj = User.objects.get(username=user)
            user_info = UserInfo.objects.get(user=user_obj)
            pro_info = UserProInfo.objects.get(user=user_obj)
            if ProConclude.objects.filter(pro_id=pro_info.id):
                info = ProConclude.objects.get(pro_id=pro_info.id)

                filename = '结题报告模板.doc'
                open_path = os.getcwd() + os.sep + 'models'
                save_path = os.getcwd() + os.sep + 'conclude'
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                file = os.path.join(open_path, filename)
                print(file)

                pro_name = pro_info.pro_name
                tutor_name = pro_info.tutor

                pro_leader = user_info.name
                leader_phone = user_info.name
                leader_sex = user_info.sex
                email = user_info.email
                major = user_info.major
                classID = user_info.classID


                savename = '结题报告_' + tutor_name + '_' + pro_leader + '_' + pro_name + '.doc'

                savepath = os.path.join(save_path, savename)
                if os.path.exists(savepath) is False:

                    pythoncom.CoInitialize()
                    try:
                        app = win32com.client.Dispatch('word.Application')
                        doc = app.Documents.Open(file)
                        print('打开的是word')
                    except:
                        app = win32com.client.Dispatch('kwps.Application')
                        doc = app.Documents.Open(file)
                        print('打开的是wps')


                    # 第一张表填写位置
                    t1 = doc.Tables[0]
                    pro_num_pos = t1.Cell(1, 2)
                    pro_name_pos = t1.Cell(2, 2)
                    pro_leader_pos = t1.Cell(3, 2)
                    leader_phone_pos = t1.Cell(4, 2)
                    tutor_id_pos = t1.Cell(5, 2)
                    leader_units_pos = t1.Cell(6, 2)
                    pro_time_pos = t1.Cell(7, 2)
                    apply_time_pos = t1.Cell(8, 2)

                    pro_num_pos.Range.ParagraphFormat.Alignment = 1
                    pro_num_pos.Range.Text = info.pro_num
                    pro_name_pos.Range.ParagraphFormat.Alignment = 1
                    pro_name_pos.Range.Text = pro_name
                    pro_leader_pos.Range.ParagraphFormat.Alignment = 1
                    pro_leader_pos.Range.Text = pro_leader
                    leader_phone_pos.Range.ParagraphFormat.Alignment = 1
                    leader_phone_pos.Range.Text = leader_phone
                    tutor_id_pos.Range.ParagraphFormat.Alignment = 1
                    tutor_id_pos.Range.Text = tutor_name
                    leader_units_pos.Range.ParagraphFormat.Alignment = 1
                    leader_units_pos.Range.Text = "深圳大学"
                    pro_time_pos.Range.ParagraphFormat.Alignment = 1
                    pro_time_pos.Range.Text = info.pro_time
                    apply_time_pos.Range.ParagraphFormat.Alignment = 1
                    apply_time_pos.Range.Text = info.fillin_time

                    t2 = doc.Tables[1]
                    pro_name1_pos = t2.Cell(1, 2)
                    pro_leader1_pos = t2.Cell(2, 3)
                    leader_sex_pos = t2.Cell(2, 5)
                    leader_ethnicity_pos = t2.Cell(2, 7)
                    leader_birth_pos = t2.Cell(2, 9)
                    leader_units1_pos = t2.Cell(3, 3)
                    leader_id_pos = t2.Cell(3, 5)
                    leader_address_pos = t2.Cell(4, 3)
                    email_pos = t2.Cell(4, 5)
                    leader_phone1_pos = t2.Cell(5, 3)

                    pro_name1_pos.Range.Text = pro_name
                    pro_leader1_pos.Range.Text = pro_leader
                    leader_sex_pos.Range.Text = leader_sex
                    leader_ethnicity_pos.Range.Text = info.leader_ethnicity
                    leader_birth_pos.Range.Text = info.leader_birth
                    leader_units1_pos.Range.Text = "深圳大学"
                    leader_id_pos.Range.Text = info.leader_id
                    leader_address_pos.Range.Text = info.leader_address
                    email_pos.Range.Text = email
                    leader_phone1_pos.Range.Text = leader_phone

                    pro_leader2_pos = t2.Cell(7, 2)
                    leader_id1_pos = t2.Cell(7, 3)
                    leader_institute_pos = t2.Cell(7, 4)
                    leader_major_class_pos = t2.Cell(7, 5)
                    leader_job_pos = t2.Cell(7, 6)
                    mem1_name_pos = t2.Cell(8, 2)
                    mem1_stuID_pos = t2.Cell(8, 3)
                    mem1_institute_pos = t2.Cell(8, 4)
                    mem1_major_class_pos = t2.Cell(8, 5)
                    mem1_job_pos = t2.Cell(8, 6)
                    mem2_name_pos = t2.Cell(9, 2)
                    mem2_stuID_pos = t2.Cell(9, 3)
                    mem2_institute_pos = t2.Cell(9, 4)
                    mem2_major_class_pos = t2.Cell(9, 5)
                    mem2_job_pos = t2.Cell(9, 6)
                    mem3_name_pos = t2.Cell(10, 2)
                    mem3_stuID_pos = t2.Cell(10, 3)
                    mem3_institute_pos = t2.Cell(10, 4)
                    mem3_major_class_pos = t2.Cell(10, 5)
                    mem3_job_pos = t2.Cell(10, 6)
                    mem4_name_pos = t2.Cell(11, 2)
                    mem4_stuID_pos = t2.Cell(11, 3)
                    mem4_institute_pos = t2.Cell(11, 4)
                    mem4_major_class_pos = t2.Cell(11, 5)
                    mem4_job_pos = t2.Cell(11, 6)

                    pro_leader2_pos.Range.Text = pro_leader
                    leader_id1_pos.Range.Text = info.leader_id
                    leader_institute_pos.Range.Text = info.leader_institute
                    leader_major_class_pos.Range.Text = major + classID
                    leader_job_pos.Range.Text = info.leader_job
                    mem1_name_pos.Range.Text = info.mem1_name
                    mem1_stuID_pos.Range.Text = info.mem1_stuID
                    mem1_institute_pos.Range.Text = info.mem1_institute
                    mem1_major_class_pos.Range.Text = info.mem1_major_class
                    mem1_job_pos.Range.Text = info.mem1_job
                    mem2_name_pos.Range.Text = info.mem2_name
                    mem2_stuID_pos.Range.Text = info.mem2_stuID
                    mem2_institute_pos.Range.Text = info.mem2_institute
                    mem2_major_class_pos.Range.Text = info.mem2_major_class
                    mem2_job_pos.Range.Text = info.mem2_job
                    mem3_name_pos.Range.Text = info.mem3_name
                    mem3_stuID_pos.Range.Text = info.mem3_stuID
                    mem3_institute_pos.Range.Text = info.mem3_institute
                    mem3_major_class_pos.Range.Text = info.mem3_major_class
                    mem3_job_pos.Range.Text = info.mem3_job
                    mem4_name_pos.Range.Text = info.mem4_name
                    mem4_stuID_pos.Range.Text = info.mem4_stuID
                    mem4_institute_pos.Range.Text = info.mem4_institute
                    mem4_major_class_pos.Range.Text = info.mem4_major_class
                    mem4_job_pos.Range.Text = info.mem4_job

                    pro_lab_pos = t2.Cell(15, 2)
                    pro_instrument_pos = t2.Cell(16, 2)
                    pro_hours_pos = t2.Cell(17, 2)
                    pro_period_status_pos = t2.Cell(19, 2)
                    pro_sum_pos = t2.Cell(21, 2)

                    pro_lab_pos.Range.Text = info.pro_lab
                    pro_instrument_pos.Range.Text = info.pro_instrument
                    # pro_hours_pos.Range.Style.Font.Underline = 1
                    pro_hours_pos.Range.InsertAfter(info.pro_hours + '小时')
                    # pro_period_status_pos.Range.Style.Font.Underline = 1
                    pro_period_status_pos.Range.InsertAfter(info.pro_period)
                    # pro_period_status_pos.Range.Style.Font.Underline = 0
                    pro_period_status_pos.Range.InsertAfter("完成情况：1.提前 2.按时 3.延期")
                    # pro_period_status_pos.Range.Style.Font.Underline = 1
                    pro_period_status_pos.Range.InsertAfter(info.pro_status)

                    pro_sum_pos.Range.Text = info.pro_sum

                    money_in_pos = t2.Cell(23, 3)
                    money_in_remark_pos = t2.Cell(23, 4)
                    money_consume_pos = t2.Cell(25, 3)
                    money_consume_remark_pos = t2.Cell(25, 4)
                    money_allowance_pos = t2.Cell(26, 3)
                    money_allowance_remark_pos = t2.Cell(26, 4)
                    money_other_pos = t2.Cell(27, 3)
                    money_other_remark_pos = t2.Cell(27, 4)
                    money_total_pos = t2.Cell(28, 3)
                    money_total_remark_pos = t2.Cell(28, 4)
                    money_rest_pos = t2.Cell(29, 3)
                    money_rest_remark_pos = t2.Cell(29, 4)

                    money_in_pos.Range.Text = info.money_in
                    money_in_remark_pos.Range.Text = info.money_in_remark
                    money_consume_pos.Range.Text = info.money_consume
                    money_consume_remark_pos.Range.Text = info.money_consume_remark
                    money_allowance_pos.Range.Text = info.money_allowance
                    money_allowance_remark_pos.Range.Text = info.money_allowance_remark
                    money_other_pos.Range.Text = info.money_other
                    money_other_remark_pos.Range.Text = info.money_other_remark
                    money_total_pos.Range.Text = info.money_total
                    money_total_remark_pos.Range.Text = info.money_total_remark
                    money_rest_pos.Range.Text = info.money_rest
                    money_rest_remark_pos.Range.Text = info.money_rest_remark

                    doc.SaveAs(savepath)
                    doc.Close()
                    app.Quit()
                    print('保存完毕')
                    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                    ProConclude.objects.get(pro_id=pro_info.id).update(export_time=date)
                print(savepath.encode('utf-8'))
                pathlist.append(savepath)
        print(pathlist)
        pathdic = {"path":pathlist}
        print('路径dic为：')
        print(pathdic)
        return JsonResponse(pathdic)
    return 'error'

def write_to_others(request):
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        print(choicelist)
        choicelist = tolist(choicelist)
        pathlist = []
        base_path = os.getcwd()
        file = 'other'
        file_dir = os.path.join(base_path, file)
        for file in choicelist:
            file_path = os.path.join(file_dir, file)
            pathlist.append(file_path)
        print(pathlist)
        pathdic = {"path": pathlist}
        return JsonResponse(pathdic)
    return 'error'

@permission_required('account.add_userproinfo',login_url="/account/login/")
def pro_mode(request):
    status_obj = Status.objects.all()[0]
    mode = status_obj.mode
    return render(request, 'manager/mode.html', {'mode': mode})

@permission_required('account.add_userproinfo',login_url="/account/login/")
def pro_mode_edit(request):
    if request.GET.get('mode'):
        mode = int(request.GET.get('mode'))
        Status.objects.all().update(mode=mode)
        return render(request, 'manager/mode.html', {'mode': mode})
    return HttpResponse('错误!')

@permission_required('account.add_userproinfo',login_url="/account/login/")
def pro_deadline(request):
    status = Status.objects.all()[0]
    date = str(status.date)
    return render(request, 'manager/date.html', {'date':date})

@permission_required('account.add_userproinfo',login_url="/account/login/")
def pro_deadline_edit(request):
    if request.GET.get('due_date',''):
        date = str(request.GET.get('due_date'))
        Status.objects.all().update(date=date)
        return render(request, 'manager/date.html', {'date': date})
    return HttpResponse('错误！')

def send_email(request):
    pro_middle = ProMiddle.objects.exclude(status=2)
    userinfo_list = []
    for i in pro_middle:
        # print(i.pro_id_id)
        userproinfo = UserProInfo.objects.get(id=i.pro_id_id)
        userinfo = UserInfo.objects.get(user_id=userproinfo.user_id)
        userinfo_dic = model_to_dict(userinfo)
        userinfo_list.append(userinfo_dic)
    return render(request,'manager/send_email.html',{"userlist":userinfo_list})
    # subject = '来自西西的问候'
    #
    # text_content = '!!!.'
    #
    # html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
    #
    # msg = EmailMultiAlternatives(subject, text_content, '492195925@qq.com', ['492195925@qq.com'])
    # # 553105821
    # # msg.attach_alternative(html_content, "text/html")
    # file = 'C:\\Users\\HP\\Desktop\\SZU\\middle\\' + '中期报告_黄淦_黄树华_基于深度学习的肌电图、脑电图分析2.doc'
    # text = open(file, 'rb').read()
    # file_name = os.path.basename(file)
    # b = make_header([(file_name, 'utf-8')]).encode('utf-8')
    # msg.attach(b, text)
    # # msg.attach_file(file)
    # msg.send()
    # return HttpResponse('成功发送！')

def modify_sub_status(request):
    if request.POST.get('choicelist','') != '':
        choicelist = eval(request.POST.get('choicelist'))[1:]
        choicelist = tolist(choicelist)
        file_class = request.POST.get('class','')
        if file_class == "apply":
            for user in choicelist:
                user_obj = User.objects.get(username=user)
                userpro_obj = UserProInfo.objects.get(user=user_obj)
                ProApply.objects.filter(pro_id=userpro_obj.id).update(status=1)
        elif file_class == "middle":
            for user in choicelist:
                user_obj = User.objects.get(username=user)
                userpro_obj = UserProInfo.objects.get(user=user_obj)
                ProMiddle.objects.filter(pro_id=userpro_obj.id).update(status=1)
        elif file_class == "conclude":
            for user in choicelist:
                user_obj = User.objects.get(username=user)
                userpro_obj = UserProInfo.objects.get(user=user_obj)
                ProConclude.objects.filter(pro_id=userpro_obj.id).update(status=1)
        else:
            return HttpResponse("出错了！")
        return HttpResponse('success')
    return HttpResponse("blank")