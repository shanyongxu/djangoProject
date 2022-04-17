#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 23:36
# @Author  : Denver.Shan
# @Site    :
# @File    : serializers.py
# @Software: PyCharm
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
