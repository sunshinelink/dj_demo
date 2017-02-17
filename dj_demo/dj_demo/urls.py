#-*-coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from mychat import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',views.index),
    url(r'^static/(?P<path>.*)$','django.contrib.staticfiles.views.serve')
]
