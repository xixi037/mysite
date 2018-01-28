from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name="user_logout"),
    # url(r'^password-change/$',views.password_change,name='password_change'),
    url(r'^password-change/$', auth_views.password_change,
        {"post_change_redirect": "/account/password-change-done", "template_name": "account/password_change.html"},
        name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done,{ "template_name": "account/password_change_done.html"},name='password_change_done'),
    url(r'^my-information/$',views.user_info,name="my_information"),
    url(r'^edit-my-information/$',views.user_info_edit,name="edit_my_information"),
    url(r'^my-pro-information/$',views.user_pro_info,name="my_pro_information"),
    url(r'^edit-my-pro-information/$',views.user_pro_info_edit,name="edit_my_pro_information"),
]