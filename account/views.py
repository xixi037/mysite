from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

import time

import os

from account.models import UserInfo, UserProInfo, ProApply, ProMiddle, ProConclude
from .forms import LoginForm, UserInfoForm, UserProInfoForm, ProApplyForm, ProMiddleForm, ProConcludeForm


# Create your views here.

@login_required(login_url='/account/login/')
def account_home(request):
    return render(request, "account/home.html")

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("账号或密码错误！")
        else:
            return HttpResponse("无效登录！")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


def password_change(request):
    return render(request, 'account/password_change.html')


@login_required(login_url='/account/login/')
def user_info(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/userinfo.html", {"user": user, "userinfo": userinfo})


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
        userinfo_form = UserInfoForm(initial={"phone": userinfo.phone, "email": userinfo.email})
        return render(request, "account/userinfo_edit.html",
                      {"user": user, "userinfo": userinfo, "userinfo_form": userinfo_form})


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
        userproinfo_form = UserProInfoForm(initial={"tutor": userproinfo.tutor, "pro_name": userproinfo.pro_name})
        return render(request, "account/proinfo_edit.html", {"user": user, "userproinfo_form": userproinfo_form})


@login_required(login_url='/account/login/')
def pro_apply_info(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userproinfo = UserProInfo.objects.get(user=user)
    proapply = ProApply.objects.get(pro_id=userproinfo)
    return render(request, "account/proapply.html",
                  {"userinfo": userinfo, "userproinfo": userproinfo, "proapply": proapply})


@login_required(login_url='/account/login/')
def pro_apply_edit(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userproinfo = UserProInfo.objects.get(user=user)
    proapply = ProApply.objects.get(pro_id=userproinfo)
    if request.method == "POST":
        proapply_form = ProApplyForm(request.POST)

        if proapply_form.is_valid():
            print('要存')
            proapply_cd = proapply_form.cleaned_data
            proapply.status = proapply_cd['status']
            proapply.pro_way = proapply_cd['pro_way']
            proapply.tutor_area = proapply_cd['tutor_area']
            proapply.tutor_phone = proapply_cd['tutor_phone']
            proapply.tutor_email = proapply_cd['tutor_email']
            proapply.leader_grade = proapply_cd['leader_grade']
            proapply.leader_area = proapply_cd['leader_area']
            proapply.leader_job = proapply_cd['leader_job']
            proapply.mem1_name = proapply_cd['mem1_name']
            proapply.mem1_sex = proapply_cd['mem1_sex']
            proapply.mem1_stuID = proapply_cd['mem1_stuID']
            proapply.mem1_grade = proapply_cd['mem1_grade']
            proapply.mem1_area = proapply_cd['mem1_area']
            proapply.mem1_job = proapply_cd['mem1_job']
            proapply.mem1_institute = proapply_cd['mem1_institute']
            proapply.mem2_name = proapply_cd['mem2_name']
            proapply.mem2_sex = proapply_cd['mem2_sex']
            proapply.mem2_stuID = proapply_cd['mem2_stuID']
            proapply.mem2_grade = proapply_cd['mem2_grade']
            proapply.mem2_area = proapply_cd['mem2_area']
            proapply.mem2_job = proapply_cd['mem2_job']
            proapply.mem2_institute = proapply_cd['mem2_institute']
            proapply.mem3_name = proapply_cd['mem3_name']
            proapply.mem3_sex = proapply_cd['mem3_sex']
            proapply.mem3_stuID = proapply_cd['mem3_stuID']
            proapply.mem3_grade = proapply_cd['mem3_grade']
            proapply.mem3_area = proapply_cd['mem3_area']
            proapply.mem3_job = proapply_cd['mem3_job']
            proapply.mem3_institute = proapply_cd['mem3_institute']
            proapply.pro_reason = proapply_cd['pro_reason']
            proapply.pro_content = proapply_cd['pro_content']
            proapply.pro_innovation = proapply_cd['pro_innovation']
            proapply.pro_source = proapply_cd['pro_source']
            proapply.time1 = proapply_cd['time1']
            proapply.content1 = proapply_cd['content1']
            proapply.leader1 = proapply_cd['leader1']
            proapply.time2 = proapply_cd['time2']
            proapply.content2 = proapply_cd['content2']
            proapply.leader2 = proapply_cd['leader2']
            proapply.time3 = proapply_cd['time3']
            proapply.content3 = proapply_cd['content3']
            proapply.leader3 = proapply_cd['leader3']
            proapply.time4 = proapply_cd['time4']
            proapply.content4 = proapply_cd['content4']
            proapply.leader4 = proapply_cd['leader4']
            proapply.time5 = proapply_cd['time5']
            proapply.content5 = proapply_cd['content5']
            proapply.leader5 = proapply_cd['leader5']
            proapply.time6 = proapply_cd['time6']
            proapply.content6 = proapply_cd['content6']
            proapply.leader6 = proapply_cd['leader6']
            proapply.time7 = proapply_cd['time7']
            proapply.content7 = proapply_cd['content7']
            proapply.leader7 = proapply_cd['leader7']
            proapply.pro_achievement = proapply_cd['pro_achievement']
            proapply.pro_endtime = proapply_cd['pro_endtime']
            proapply.pro_form = proapply_cd['pro_form']
            proapply.pro_participant = proapply_cd['pro_participant']
            proapply.budget_equip_money = proapply_cd['budget_equip_money']
            proapply.budget_equip_reason = proapply_cd['budget_equip_reason']
            proapply.budget_material_money = proapply_cd['budget_material_money']
            proapply.budget_material_reason = proapply_cd['budget_material_reason']
            proapply.budget_meeting_money = proapply_cd['budget_meeting_money']
            proapply.budget_meeting_reason = proapply_cd['budget_meeting_reason']
            proapply.budget_apply_money = proapply_cd['budget_apply_money']
            proapply.budget_apply_reason = proapply_cd['budget_apply_reason']
            proapply.budget_books_money = proapply_cd['budget_books_money']
            proapply.budget_books_reason = proapply_cd['budget_books_reason']
            proapply.budget_trans_money = proapply_cd['budget_trans_money']
            proapply.budget_trans_reason = proapply_cd['budget_trans_reason']
            proapply.budget_service_money = proapply_cd['budget_service_money']
            proapply.budget_service_reason = proapply_cd['budget_service_reason']
            proapply.budget_other_money = proapply_cd['budget_other_money']
            proapply.budget_other_reason = proapply_cd['budget_other_reason']
            proapply.budget_total_money = proapply_cd['budget_total_money']
            proapply.leader7 = proapply_cd['leader7']
            proapply.fillin_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            proapply.save()
        return HttpResponseRedirect('/account/my-pro-apply/')
    else:
        proapply_form = ProApplyForm(initial={"pro_way": proapply.pro_way, "tutor_area": proapply.tutor_area,
                                              "tutor_phone": proapply.tutor_phone, "tutor_email": proapply.tutor_email,
                                              "leader_grade": proapply.leader_grade,
                                              "leader_area": proapply.leader_area, "leader_job": proapply.leader_job,
                                              "mem1_name": proapply.mem1_name, "mem1_sex": proapply.mem1_sex,
                                              "mem1_stuID": proapply.mem1_stuID, "mem1_grade": proapply.mem1_grade,
                                              "mem1_area": proapply.mem1_area, "mem1_job": proapply.mem1_job,
                                              "mem1_institute": proapply.mem1_institute,
                                              "mem2_name": proapply.mem2_name,
                                              "mem2_sex": proapply.mem2_sex, "mem2_stuID": proapply.mem2_stuID,
                                              "mem2_grade": proapply.mem2_grade, "mem2_area": proapply.mem2_area,
                                              "mem2_job": proapply.mem2_job, "mem2_institute": proapply.mem2_institute,
                                              "mem3_name": proapply.mem3_name, "mem3_sex": proapply.mem3_sex,
                                              "mem3_stuID": proapply.mem3_stuID, "mem3_grade": proapply.mem3_grade,
                                              "mem3_area": proapply.mem3_area, "mem3_job": proapply.mem3_job,
                                              "mem3_institute": proapply.mem3_institute,
                                              "pro_reason": proapply.pro_reason, "pro_content": proapply.pro_content,
                                              "pro_innovation": proapply.pro_innovation,
                                              "pro_source": proapply.pro_source, "time1": proapply.time1,
                                              "content1": proapply.content1, "leader1": proapply.leader1,
                                              "time2": proapply.time2, "time3": proapply.time3, "time4": proapply.time4,
                                              "time5": proapply.time5, "time6": proapply.time6, "time7": proapply.time7,
                                              "content2": proapply.content2, "content3": proapply.content3,
                                              "content4": proapply.content4, "content5": proapply.content5,
                                              "content6": proapply.content6, "content7": proapply.content7,
                                              "leader2": proapply.leader2, "leader3": proapply.leader3,
                                              "leader4": proapply.leader4, "leader5": proapply.leader5,
                                              "leader6": proapply.leader6, "leader7": proapply.leader7,
                                              "pro_achievement": proapply.pro_achievement,
                                              "pro_endtime": proapply.pro_endtime, "pro_form": proapply.pro_form,
                                              "pro_participant": proapply.pro_participant,
                                              "budget_equip_money": proapply.budget_equip_money,
                                              "budget_equip_reason": proapply.budget_equip_reason,
                                              "budget_material_money": proapply.budget_material_money,
                                              "budget_material_reason": proapply.budget_material_reason,
                                              "budget_meeting_money": proapply.budget_meeting_money,
                                              "budget_meeting_reason": proapply.budget_meeting_reason,
                                              "budget_apply_money": proapply.budget_apply_money,
                                              "budget_apply_reason": proapply.budget_apply_reason,
                                              "budget_books_money": proapply.budget_books_money,
                                              "budget_books_reason": proapply.budget_books_reason,
                                              "budget_trans_money": proapply.budget_trans_money,
                                              "budget_trans_reason": proapply.budget_trans_reason,
                                              "budget_service_money": proapply.budget_service_money,
                                              "budget_service_reason": proapply.budget_service_reason
                                              })
        if proapply.status == '2':
            return HttpResponseRedirect('/account/my-pro-apply/')
        return render(request, "account/proapply_edit.html",
                      {"userinfo": userinfo, "userproinfo": userproinfo, "proapply_form": proapply_form})


@login_required(login_url='/account/login/')
def pro_middle_info(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userproinfo = UserProInfo.objects.get(user=user)
    promiddle = ProMiddle.objects.get(pro_id=userproinfo)
    return render(request, "account/promiddle.html",
                  {"userinfo": userinfo, "userproinfo": userproinfo, "promiddle": promiddle})


@login_required(login_url='/account/login/')
def pro_middle_info_edit(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userproinfo = UserProInfo.objects.get(user=user)
    promiddle = ProMiddle.objects.get(pro_id=userproinfo)
    if request.method == "POST":
        promiddle_form = ProMiddleForm(request.POST)

        if promiddle_form.is_valid():
            promiddle_cd = promiddle_form.cleaned_data
            promiddle.status = promiddle_cd['status']
            promiddle.pro_num = promiddle_cd["pro_num"]
            promiddle.pro_mems = promiddle_cd["pro_mems"]
            promiddle.pro_endtime = promiddle_cd["pro_endtime"]
            promiddle.pro_etime = promiddle_cd["pro_etime"]
            promiddle.pro_stime = promiddle_cd["pro_stime"]
            promiddle.pro_schedule = promiddle_cd["pro_schedule"]
            promiddle.pro_source = promiddle_cd["pro_source"]
            promiddle.pro_money = promiddle_cd["pro_money"]
            promiddle.pro_difficulties = promiddle_cd["pro_difficulties"]
            promiddle.pro_advice = promiddle_cd["pro_advice"]
            promiddle.pro_change = promiddle_cd["pro_change"]
            promiddle.pro_plan = promiddle_cd["pro_plan"]
            promiddle.pro_harvest = promiddle_cd["pro_harvest"]
            promiddle.save()
        return HttpResponseRedirect('/account/my-pro-middle/')
    else:
        promiddle_form = ProMiddleForm(
            initial={"pro_num": promiddle.pro_num, "pro_mems": promiddle.pro_mems, "pro_endtime": promiddle.pro_endtime,
                     "pro_etime": promiddle.pro_etime, "pro_stime": promiddle.pro_stime,
                     "pro_schedule": promiddle.pro_schedule, "pro_source": promiddle.pro_source,
                     "pro_money": promiddle.pro_money, "pro_difficulties": promiddle.pro_difficulties,
                     "pro_advice": promiddle.pro_advice, "pro_change": promiddle.pro_change,
                     "pro_plan": promiddle.pro_plan, "pro_harvest": promiddle.pro_harvest})
        if promiddle.status == '2':
            return HttpResponseRedirect('/account/my-pro-middle/')
        return render(request, "account/promiddle_edit.html",
                      {"userinfo": userinfo, "userproinfo": userproinfo, "promiddle_form": promiddle_form})


@login_required(login_url='/account/login/')
def pro_conclude_info(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userproinfo = UserProInfo.objects.get(user=user)
    proconclude = ProConclude.objects.get(pro_id=userproinfo)
    return render(request, "account/proconclude.html",
                  {"userinfo": userinfo, "userproinfo": userproinfo, "proconclude": proconclude})


@login_required(login_url='/account/login/')
def pro_conclude_info_edit(request):
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    userproinfo = UserProInfo.objects.get(user=user)
    proconclude = ProConclude.objects.get(pro_id=userproinfo)
    if request.method == "POST":
        proconclude_form = ProConcludeForm(request.POST)

        if proconclude_form.is_valid():
            proconclude_cd = proconclude_form.cleaned_data
            proconclude.status = proconclude_cd['status']
            proconclude.pro_num = proconclude_cd["pro_num"]
            proconclude.pro_time = proconclude_cd["pro_time"]
            proconclude.leader_ethnicity = proconclude_cd["leader_ethnicity"]
            proconclude.leader_birth = proconclude_cd["leader_birth"]
            proconclude.leader_address = proconclude_cd["leader_address"]
            proconclude.leader_job = proconclude_cd["leader_job"]
            proconclude.mem1_name = proconclude_cd["mem1_name"]
            proconclude.mem1_stuID = proconclude_cd["mem1_stuID"]
            proconclude.mem1_institute = proconclude_cd["mem1_institute"]
            proconclude.mem1_major_class = proconclude_cd["mem1_major_class"]
            proconclude.mem1_job = proconclude_cd["mem1_job"]
            proconclude.mem2_name = proconclude_cd["mem2_name"]
            proconclude.mem2_stuID = proconclude_cd["mem2_stuID"]
            proconclude.mem2_institute = proconclude_cd["mem2_institute"]
            proconclude.mem2_major_class = proconclude_cd["mem2_major_class"]
            proconclude.mem2_job = proconclude_cd["mem2_job"]
            proconclude.mem3_name = proconclude_cd["mem3_name"]
            proconclude.mem3_stuID = proconclude_cd["mem3_stuID"]
            proconclude.mem3_institute = proconclude_cd["mem3_institute"]
            proconclude.mem3_major_class = proconclude_cd["mem3_major_class"]
            proconclude.mem3_job = proconclude_cd["mem3_job"]
            proconclude.mem4_name = proconclude_cd["mem4_name"]
            proconclude.mem4_stuID = proconclude_cd["mem4_stuID"]
            proconclude.mem4_institute = proconclude_cd["mem4_institute"]
            proconclude.mem4_major_class = proconclude_cd["mem4_major_class"]
            proconclude.mem4_job = proconclude_cd["mem4_job"]
            proconclude.pro_lab = proconclude_cd["pro_lab"]
            proconclude.pro_instrument = proconclude_cd["pro_instrument"]
            proconclude.pro_hours = proconclude_cd["pro_hours"]
            proconclude.pro_period = proconclude_cd["pro_period"]
            proconclude.pro_status = proconclude_cd["pro_status"]
            proconclude.pro_sum = proconclude_cd["pro_sum"]
            proconclude.money_in = proconclude_cd["money_in"]
            proconclude.money_in_remark = proconclude_cd["money_in_remark"]
            proconclude.money_consume = proconclude_cd["money_consume"]
            proconclude.money_consume_remark = proconclude_cd["money_consume_remark"]
            proconclude.money_allowance = proconclude_cd["money_allowance"]
            proconclude.money_allowance_remark = proconclude_cd["money_allowance_remark"]
            proconclude.money_other = proconclude_cd["money_other"]
            proconclude.money_other_remark = proconclude_cd["money_other_remark"]
            proconclude.money_total = proconclude_cd["money_total"]
            proconclude.money_total_remark = proconclude_cd["money_total_remark"]
            proconclude.money_rest = proconclude_cd["money_rest"]
            proconclude.money_rest_remark = proconclude_cd["money_rest_remark"]
            proconclude.save()
        return HttpResponseRedirect('/account/my-pro-conclude/')
    else:
        proconclude_form = ProConcludeForm(
            initial={"pro_num": proconclude.pro_num, "pro_time": proconclude.pro_time,
                     "leader_ethnicity": proconclude.leader_ethnicity,"leader_birth": proconclude.leader_birth,
                     "leader_address": proconclude.leader_address, "leader_job": proconclude.leader_job,
                     "mem1_name": proconclude.mem1_name, "mem1_stuID": proconclude.mem1_stuID,
                     "mem1_institute": proconclude.mem1_institute, "mem1_major_class": proconclude.mem1_major_class,
                     "mem1_job": proconclude.mem1_job, "mem2_name": proconclude.mem2_name,
                     "mem2_stuID": proconclude.mem2_stuID, "mem2_institute": proconclude.mem2_institute,
                     "mem2_major_class": proconclude.mem2_major_class, "mem2_job": proconclude.mem2_job,
                     "mem3_name": proconclude.mem3_name, "mem3_stuID": proconclude.mem3_stuID,
                     "mem3_institute": proconclude.mem3_institute, "mem3_major_class": proconclude.mem3_major_class,
                     "mem3_job": proconclude.mem3_job, "mem4_name": proconclude.mem4_name,
                     "mem4_stuID": proconclude.mem4_stuID, "mem4_institute": proconclude.mem4_institute,
                     "mem4_major_class": proconclude.mem4_major_class, "mem4_job": proconclude.mem4_job,
                     "pro_lab": proconclude.pro_lab, "pro_instrument": proconclude.pro_instrument,
                     "pro_hours": proconclude.pro_hours, "pro_period": proconclude.pro_period,
                     "pro_status": proconclude.pro_status, "pro_sum": proconclude.pro_sum,
                     "money_in": proconclude.money_in, "money_in_remark": proconclude.money_in_remark,
                     "money_consume": proconclude.money_consume,
                     "money_consume_remark": proconclude.money_consume_remark,
                     "money_allowance": proconclude.money_allowance,
                     "money_allowance_remark": proconclude.money_allowance_remark,
                     "money_other": proconclude.money_other, "money_other_remark": proconclude.money_other_remark,
                     "money_total": proconclude.money_total, "money_total_remark": proconclude.money_total_remark,
                     "money_rest": proconclude.money_rest, "money_rest_remark": proconclude.money_rest_remark})
        if proconclude.status == '2':
            return HttpResponseRedirect('/account/my-pro-conclude/')
        return render(request, "account/proconclude_edit.html",
                      {"userinfo": userinfo, "userproinfo": userproinfo, "proconclude_form": proconclude_form})

@login_required(login_url='/account/login/')
def upload_conclude(request):
    print(request.method)
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        userinfo = UserInfo.objects.get(user=user)
        userproinfo = UserProInfo.objects.get(user=user)
        tutor = userproinfo.tutor
        name = userinfo.name
        pro_name = userproinfo.pro_name
        path = os.getcwd() + os.sep + 'other'
        if not os.path.exists(path):
            os.makedirs(path)
        if request.FILES.get('experiment_file','') != '':
            file_obj = request.FILES.get('experiment_file')
            savename = '实验报告_' + tutor + '_' + name + '_' + pro_name + '.doc'
            filepath = os.path.join(path, savename)
            print(filepath)
            dest = open(filepath, 'wb+')
            dest.write(file_obj.read())
            dest.close()
            return render(request, 'account/conclude_upload.html', {'status1': '上传成功！'})
        if request.FILES.get('research_file', '') != '':
            file_obj = request.FILES.get('research_file')
            savename = '研究报告_' + tutor + '_' + name + '_' + pro_name + '.doc'
            filepath = os.path.join(path, savename)
            print(filepath)
            dest = open(filepath, 'wb+')
            dest.write(file_obj.read())
            dest.close()
            return render(request,'account/conclude_upload.html', {'status2': '上传成功！'})
        if request.FILES.get('compressed_file', '') != '':
            file_obj = request.FILES.get('compressed_file')
            savename = '压缩文件_' + tutor + '_' + name + '_' + pro_name + '.zip'
            filepath = os.path.join(path, savename)
            print(filepath)
            dest = open(filepath, 'wb+')
            dest.write(file_obj.read())
            dest.close()
            return render(request, 'account/conclude_upload.html', {'status3': '上传成功！'})
    # else:
    return render(request,"account/conclude_upload.html")