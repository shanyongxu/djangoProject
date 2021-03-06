#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 0:09
# @Author  : Denver.Shan
# @Site    :
# @File    : serializers.py
# @Software: PyCharm
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# 将 modelserializer替换为HyperlinkedModelSeralizer
# 这两个Serializer有以下几点不同
# 1.HyperLinked默认情况下不包括id字段，注意，这是默认情况，可以手动设置ID
# 2.HyperLinked包含一个url字段，使用HyperLinkedIndentityField
# 3.关联关系使用HyperlinkedRelatedField，而不是PrimaryKeyRelatedField
#
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']

# class SnippetSerializer(serializers.ModelSerializer):
#     # 这里的序列化器其实和django form类似, 如果使用ModelSerializer下面的代码就可以注释掉了
#     # id = serializers.IntegerField(read_only=True)
#     # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # code = serializers.CharField(style={'base_template': 'textarea.html'})
#     # linenos = serializers.BooleanField(required=False)
#     # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
#
#     # def create(self, validated_data):
#     #     # post方法，创建
#     #     print(validated_data)
#     #     return Snippet.objects.create(**validated_data)
#
#     # def update(self, instance, validated_data):
#     #     # update方法，修改
#     #     instance.title = validated_data.get('title', instance.title)
#     #     instance.code = validated_data.get('code', instance.code)
#     #     instance.linenos = validated_data.get('linenos', instance.linenos)
#     #     instance.language = validated_data.get('language', instance.language)
#     #     instance.style = validated_data.get('style', instance.style)
#     #     instance.save()
#     #     return instance

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
