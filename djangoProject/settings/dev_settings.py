#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 23:27
# @Author  : Denver.Shan
# @Site    :
# @File    : dev_settings.py
# @Software: PyCharm
from .base import *
# import sys
# import os
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
# sys.path.insert(0, os.path.join(BASE_DIR, 'settings'))
# REF的配置

INSTALLED_APPS += [
    'rest_framework',
    'quickstart',
    'snippets',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    # 如果单纯设置page_size则可能会出现一个警告
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
