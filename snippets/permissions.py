#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 17:17
# @Author  : Denver.Shan
# @Site    :
# @File    : permissions.py
# @Software: PyCharm
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限，只允许代码片段的作者有编辑权限
    """

    def has_object_permission(self, request, view, obj):
        '''
        读取权限允许任何请求
        :param request:
        :param view:
        :param obj:
        :return:
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
