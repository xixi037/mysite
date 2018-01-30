from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#用户信息
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

    class Meta:
        permissions = (
            ('add_userproinfo', u"添加用户"),  # 权限字段名称及其解释
            ('del_userproinfo', u"删除用户"),
            ('edit_own_customer_info', u"修改用户信息"),
        )

#项目信息
class UserProInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    pro_name = models.CharField(max_length=255, blank=True, null=True, default='')
    tutor = models.CharField(max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return "user:{}".format(self.user.username)

class ProApply(models.Model):
    pro_id = models.OneToOneField(UserProInfo, unique=True)
    export_time = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, blank=True, default='')
    fillin_time = models.CharField(max_length=255, blank=True, default='')
    pro_way = models.CharField(max_length=255, blank=True, default='')
    tutor_area = models.CharField(max_length=255, blank=True, default='')
    tutor_phone = models.CharField(max_length=255, blank=True, default='')
    tutor_email = models.CharField(max_length=255, blank=True, default='')
    leader_grade = models.CharField(max_length=255, blank=True, default='')
    leader_area = models.CharField(max_length=255, blank=True, default='')
    leader_job = models.CharField(max_length=255, blank=True, default='')
    mem1_name = models.CharField(max_length=255, blank=True, default='')
    mem1_sex = models.CharField(max_length=255, blank=True, default='')
    mem1_stuID = models.CharField(max_length=255, blank=True, default='')
    mem1_grade = models.CharField(max_length=255, blank=True, default='')
    mem1_area = models.CharField(max_length=255, blank=True, default='')
    mem1_job = models.CharField(max_length=255, blank=True, default='')
    mem1_institute = models.CharField(max_length=255, blank=True, default='')
    mem2_name = models.CharField(max_length=255, blank=True, default='')
    mem2_sex = models.CharField(max_length=255, blank=True, default='')
    mem2_stuID = models.CharField(max_length=255, blank=True, default='')
    mem2_grade = models.CharField(max_length=255, blank=True, default='')
    mem2_area = models.CharField(max_length=255, blank=True, default='')
    mem2_job = models.CharField(max_length=255, blank=True, default='')
    mem2_institute = models.CharField(max_length=255, blank=True, default='')
    mem3_name = models.CharField(max_length=255, blank=True, default='')
    mem3_sex = models.CharField(max_length=255, blank=True, default='')
    mem3_stuID = models.CharField(max_length=255, blank=True, default='')
    mem3_grade = models.CharField(max_length=255, blank=True, default='')
    mem3_area = models.CharField(max_length=255, blank=True, default='')
    mem3_job = models.CharField(max_length=255, blank=True, default='')
    mem3_institute = models.CharField(max_length=255, blank=True, default='')
    pro_reason = models.TextField(blank=True, default='')
    pro_content = models.TextField(blank=True, default='')
    pro_innovation = models.TextField(blank=True, default='')
    pro_source = models.TextField(blank=True, default='')
    time1 = models.CharField(max_length=255, blank=True, default='')
    content1 = models.CharField(max_length=255, blank=True, default='')
    leader1 = models.CharField(max_length=255, blank=True, default='')
    time2 = models.CharField(max_length=255, blank=True, default='')
    time3 = models.CharField(max_length=255, blank=True, default='')
    time4 = models.CharField(max_length=255, blank=True, default='')
    time5 = models.CharField(max_length=255, blank=True, default='')
    time6 = models.CharField(max_length=255, blank=True, default='')
    time7 = models.CharField(max_length=255, blank=True, default='')
    content2 = models.CharField(max_length=255, blank=True, default='')
    content3 = models.CharField(max_length=255, blank=True, default='')
    content4 = models.CharField(max_length=255, blank=True, default='')
    content5 = models.CharField(max_length=255, blank=True, default='')
    content6 = models.CharField(max_length=255, blank=True, default='')
    content7 = models.CharField(max_length=255, blank=True, default='')
    leader2 = models.CharField(max_length=255, blank=True, default='')
    leader3 = models.CharField(max_length=255, blank=True, default='')
    leader4 = models.CharField(max_length=255, blank=True, default='')
    leader5 = models.CharField(max_length=255, blank=True, default='')
    leader6 = models.CharField(max_length=255, blank=True, default='')
    leader7 = models.CharField(max_length=255, blank=True, default='')
    pro_achievement = models.CharField(max_length=255, blank=True, default='')
    pro_endtime = models.CharField(max_length=255, blank=True, default='')
    pro_form = models.CharField(max_length=255, blank=True, default='')
    pro_participant = models.CharField(max_length=255, blank=True, default='')
    budget_equip_money = models.CharField(max_length=255, blank=True, default='')
    budget_equip_reason = models.CharField(max_length=255, blank=True, default='')
    budget_material_money = models.CharField(max_length=255, blank=True, default='')
    budget_material_reason = models.CharField(max_length=255, blank=True, default='')
    budget_meeting_money = models.CharField(max_length=255, blank=True, default='')
    budget_meeting_reason = models.CharField(max_length=255, blank=True, default='')
    budget_apply_money = models.CharField(max_length=255, blank=True, default='')
    budget_apply_reason = models.CharField(max_length=255, blank=True, default='')
    budget_books_money = models.CharField(max_length=255, blank=True, default='')
    budget_books_reason = models.CharField(max_length=255, blank=True, default='')
    budget_trans_money = models.CharField(max_length=255, blank=True, default='')
    budget_trans_reason = models.CharField(max_length=255, blank=True, default='')
    budget_service_money = models.CharField(max_length=255, blank=True, default='')
    budget_service_reason = models.CharField(max_length=255, blank=True, default='')
    budget_other_money = models.CharField(max_length=255, blank=True, default='')
    budget_other_reason = models.CharField(max_length=255, blank=True, default='')
    budget_total_money = models.CharField(max_length=255, blank=True, default='')

class ProMiddle(models.Model):
    pro_id = models.OneToOneField(UserProInfo, unique=True)
    export_time = models.CharField(max_length=255, blank=True, default='')
    status = models.CharField(max_length=1, blank=True, default='')
    pro_num = models.CharField(max_length=255, blank=True, default='')
    pro_mems = models.CharField(max_length=255, blank=True, default='')
    pro_endtime = models.CharField(max_length=255, blank=True, default='')
    pro_etime = models.CharField(max_length=255, blank=True, default='')
    pro_stime = models.CharField(max_length=255, blank=True, default='')
    pro_schedule = models.TextField(blank=True, default='')
    pro_source = models.TextField(blank=True, default='')
    pro_money = models.TextField(blank=True, default='')
    pro_difficulties = models.TextField(blank=True, default='')
    pro_advice = models.TextField(blank=True, default='')
    pro_change = models.TextField(blank=True, default='')
    pro_plan = models.TextField(blank=True, default='')
    pro_harvest = models.TextField(blank=True, default='')

class ProConclude(models.Model):
    pro_id = models.OneToOneField(UserProInfo, unique=True)
    status = models.CharField(max_length=1, blank=True, default='')
    fillin_time = models.CharField(max_length=255, blank=True, default='')
    export_time = models.CharField(max_length=255, blank=True, default='')
    pro_num = models.CharField(max_length=255, blank=True, default='')
    pro_mems = models.CharField(max_length=255, blank=True, default='')
    pro_time = models.CharField(max_length=255, blank=True, default='')
    leader_ethnicity = models.CharField(max_length=255, blank=True, default='')
    leader_birth = models.CharField(max_length=255, blank=True, default='')
    leader_address = models.CharField(max_length=255, blank=True, default='')
    leader_institute = models.CharField(max_length=255, blank=True, default='')
    leader_job = models.CharField(max_length=255, blank=True, default='')
    mem1_name = models.CharField(max_length=255, blank=True, default='')
    mem1_stuID = models.CharField(max_length=255, blank=True, default='')
    mem1_institute = models.CharField(max_length=255, blank=True, default='')
    mem1_major_class = models.CharField(max_length=255, blank=True, default='')
    mem1_job = models.CharField(max_length=255, blank=True, default='')
    mem2_name = models.CharField(max_length=255, blank=True, default='')
    mem2_stuID = models.CharField(max_length=255, blank=True, default='')
    mem2_institute = models.CharField(max_length=255, blank=True, default='')
    mem2_major_class = models.CharField(max_length=255, blank=True, default='')
    mem2_job = models.CharField(max_length=255, blank=True, default='')
    mem3_name = models.CharField(max_length=255, blank=True, default='')
    mem3_stuID = models.CharField(max_length=255, blank=True, default='')
    mem3_institute = models.CharField(max_length=255, blank=True, default='')
    mem3_major_class = models.CharField(max_length=255, blank=True, default='')
    mem3_job = models.CharField(max_length=255, blank=True, default='')
    mem4_name = models.CharField(max_length=255, blank=True, default='')
    mem4_stuID = models.CharField(max_length=255, blank=True, default='')
    mem4_institute = models.CharField(max_length=255, blank=True, default='')
    mem4_major_class = models.CharField(max_length=255, blank=True, default='')
    mem4_job = models.CharField(max_length=255, blank=True, default='')
    pro_lab = models.TextField(blank=True, default='')
    pro_instrument = models.TextField(blank=True, default='')
    pro_hours = models.CharField(max_length=255, blank=True, default='')
    pro_period = models.CharField(max_length=255, blank=True, default='')
    pro_status = models.CharField(max_length=255, blank=True, default='')
    pro_sum = models.TextField(blank=True, default='')
    money_in = models.CharField(max_length=255, blank=True, default='')
    money_in_remark = models.CharField(max_length=255, blank=True, default='')
    money_consume = models.CharField(max_length=255, blank=True, default='')
    money_consume_remark = models.CharField(max_length=255, blank=True, default='')
    money_allowance = models.CharField(max_length=255, blank=True, default='')
    money_allowance_remark = models.CharField(max_length=255, blank=True, default='')
    money_other = models.CharField(max_length=255, blank=True, default='')
    money_other_remark = models.CharField(max_length=255, blank=True, default='')
    money_total = models.CharField(max_length=255, blank=True, default='')
    money_total_remark = models.CharField(max_length=255, blank=True, default='')
    money_rest = models.CharField(max_length=255, blank=True, default='')
    money_rest_remark = models.CharField(max_length=255, blank=True, default='')