from django.conf.urls import url
from . import views

app_name ='polls' # 用于区分不同app
urlpatterns=[

    url(r'^$',views.index,name='index'),

    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),

    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),

    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]