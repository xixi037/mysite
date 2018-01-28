from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.panel_home, name="panel_home"),
    # url(r'^mypro', views.panel_mypro, name="panel_mypro"),
]