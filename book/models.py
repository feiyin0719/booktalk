#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from booktalk.settings import AUTH_USER_MODEL



class Article(models.Model):
    owner=models.ForeignKey(AUTH_USER_MODEL,verbose_name=u'作者')
    title=models.TextField(verbose_name=u'标题')
    content=models.TextField(verbose_name=u'内容')
    cover=models.ImageField(verbose_name=u'封面',upload_to='article/cover',blank=True,null=True)
    type = models.IntegerField(default=0, verbose_name=u'订单状态', choices=((0,u'读书心得'),(1,u'好书推荐')))
    createdate=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name=u'文章'
        verbose_name_plural = u'文章'
    def __unicode__(self):
        return self.title