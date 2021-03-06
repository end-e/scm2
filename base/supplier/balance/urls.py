"""scm URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from base.supplier.balance.views import *

urlpatterns = [
    url(r'^balance/$', balance , name='balance'),
    url(r'^balance/balanceArticle/', balanceArticle, name='balanceArticle'),
    #add by liubf at 2016/01/12
    url(r'^balance/apply/edit/', applyEdit, name='applyEdit'),
    url(r'^balance/apply/save/', applySave, name='applySave'),
    url(r'^balance/apply/findSheet/', findSheet, name='findSheet'),
     url(r'^balance/apply/findKxlist/', findKxlist, name='findKxlist'),
    #end by liubf at 2016/01/12
]
