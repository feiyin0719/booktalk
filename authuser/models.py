#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.safestring import mark_safe
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MyUser(AbstractUser):
    nickname = models.CharField(max_length=255, verbose_name=u'昵称', null=True, blank=True)
    headImage = models.ImageField(upload_to='headimage', null=True, blank=True, verbose_name=u'头像')
    profile = models.CharField(max_length=255, verbose_name=u'个人描述', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name=u'手机', blank=True, null=True)
    zhifubao = models.CharField(verbose_name=u'支付宝', default='', max_length=32, blank=True, null=True)
    enable = models.BooleanField(verbose_name=u'是否启用', default=True)
    objects = UserManager()

    def headimg(self):
        if self.headImage:
            mark_safe(
                '<a href=%s target="_blank" title="头像" data-gallery="gallery"><img src=%s height="50" width="50" class="field_img"> </a>' % (
                None if not self.headImage else self.headImage.url, None if not self.headImage else self.headImage.url))
        else:
            return mark_safe('')

    headimg.short_description = u'头像'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    def __str__(self):
        return self.username
    def __unicode__(self):
        return self.username
class Test1(models.Model):
    name=models.CharField(max_length=12)
class Test2(models.Model):
    name=models.CharField(max_length=12)
    test=models.ForeignKey(Test1)
class Test3(models.Model):
    name=models.CharField(max_length=12)
    test2=models.ManyToManyField(Test2)