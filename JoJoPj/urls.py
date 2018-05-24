"""JoJoPj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),                  # 管理员
    url(r'^$',        'JoJo.views.homepage', name='main'),      # 默认访问登录页面
    url(r'^login/$',  'JoJo.views.login', name='login'),        # 登录页面
    url(r'^regist/$', 'JoJo.views.regist', name='regist'),      # 注册
    url(r'^test/$', 'JoJo.views.test', name='test'),
    url(r'^study/$',  'JoJo.views.study', name='index'),
    url(r'^logout/$', 'JoJo.views.logout', name='logout'),
    url(r'^share/$',  'JoJo.views.share', name='share'),
    url(r'^profile/$',  'JoJo.views.profile', name='profile'),  # 个人主页
    url(r'^ajax_list/$', 'JoJo.views.ajax_list', name='ajax-list'),
    url(r'^getNextWord/$', 'JoJo.views.getNextWord', name='getNextWord'),
]
