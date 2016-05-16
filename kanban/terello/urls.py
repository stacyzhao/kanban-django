from django.conf.urls import url, include
from rest_framework import routers
from terello import views
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^tasks/$', views.TaskViewSet.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    ]
