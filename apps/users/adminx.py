#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : adminx.py.py
# @Author: 韩朝彪
# @Date  : 2018/3/7
# @Desc  :
# Xadmin会自动搜寻这种命名的文件。
import xadmin

from .models import EmailVerifyRecord
from .models import Banner


# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列 list_display可以使用列表或元祖，建议使用列表。否则元组只有一个元素，忘记加逗号就会报错。
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 注册时 模型类必须放前面
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
