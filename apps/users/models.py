# encoding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


# 扩充系统django user表, 继承django 点进AbstractUser可以看到这个models里面就有我们默认表的那些字段。
@python_2_unicode_compatible
class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    nick_name = models.CharField(max_length=40, verbose_name=u'昵称', default='')
    # 生日，可以为空
    birthday = models.DateTimeField(null=True, blank=True, verbose_name=u'生日')
    # 性别 只能男或女，默认女
    gender = models.CharField(max_length=6, verbose_name=u'性别', choices=GENDER_CHOICES, default='female')
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'电话')
    # 头像 默认使用default.png
    image = models.ImageField(upload_to='image/%Y/%m', default='default.png', max_length=100)

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载Unicode方法，打印实例会打印username，username为继承自abstractuser
    #  # 重载Unicode方法使后台不再直接显示object
    def __str__(self):
        return self.username


# 邮箱验证码model
@python_2_unicode_compatible
class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码")
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=10, verbose_name=u'发送类型')
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')
    # 字段的verbose_name会直接显示在后台

    class Meta:
        # 显示在菜单栏
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}//{1}'.format(self.code, self.email)


# 轮播图model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")

    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

"""
与用户相关的评论啊，点赞啊。学习的课程啊并没有放进来，因为那些独立性不高。
容易产生循环引用。我们把那些放到operation中。
"""