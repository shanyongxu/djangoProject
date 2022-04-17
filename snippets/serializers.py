#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 0:09
# @Author  : Denver.Shan
# @Site    :
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    # 这里的序列化器其实和django form类似, 如果使用ModelSerializer下面的代码就可以注释掉了
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    # def create(self, validated_data):
    #     # post方法，创建
    #     print(validated_data)
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # update方法，修改
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
