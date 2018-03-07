# encoding: utf-8
from django.contrib import admin
from .models import UserProfile
# Register your models here.
import xadmin
"""
在Django的admin中可以把上章的表都注册进来。对于表进行任意的增删改查。
默认其实会把user也注册进来的，但是因为我们通过userProfile覆盖了user。所以没有显示。
"""


# 写一个管理器:命名, model+Admin
# class UserProfileAdmin(admin.ModelAdmin):
#     pass

# 将UserProfile注册进我们的admin中, 并为它选择管理器
# admin.site.register(UserProfile, UserProfileAdmin)
