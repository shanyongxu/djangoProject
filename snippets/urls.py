#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 14:39
# @Author  : Denver.Shan
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path(r'snippets/', views.SnippetList.as_view()),
    path(r'snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path(r'users/', views.UserList.as_view()),
    path(r'users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
