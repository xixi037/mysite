from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manager_home, name="manager_home"),
    # url(r'^mypro', views.panel_mypro, name="panel_mypro"),
]