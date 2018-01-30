from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manager_home, name="manager_home"),
    url(r'^userlist', views.userlist, name="userlist"),
    url(r'^del-userlist', views.del_userlist, name="del_userlist"),
    url(r'^apply-infolist', views.apply_infolist, name="apply_infolist"),
    url(r'^middle-infolist', views.middle_infolist, name="middle_infolist"),
    url(r'^conclude-infolist', views.conclude_infolist, name="conclude_infolist"),
    url(r'^others-infolist', views.others_infolist, name="others_infolist"),
    url(r'^write-to-apply', views.write_to_apply, name="write_to_apply"),
    url(r'^write-to-middle', views.write_to_middle, name="write_to_middle"),
    url(r'^write-to-conclude', views.write_to_conclude, name="write_to_conclude"),
    url(r'^write-to-others', views.write_to_others, name="write_to_others"),
    url(r'^pro-mode',views.pro_mode,name="pro_mode"),
    url(r'^edit-pro-mode',views.pro_mode_edit,name="pro_mode_edit"),
    url(r'^pro-deadline',views.pro_deadline,name="pro_deadline"),
    url(r'^edit-pro-deadline',views.pro_deadline_edit,name="pro_deadline_edit"),
]