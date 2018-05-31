from django.conf.urls import url
from django.urls import path
from . import views

app_name ='App' # 用于区分不同app
urlpatterns=[
    #url(r'welcome/$',views.welcome,name='welcome'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^login/$',views.login,name = 'login'),
    path('',views.index,name='index'),
    #url(r'^index/$',views.index,name = 'index'),
    # url(r'^logout/$',views.logout,name = 'logout'),
]