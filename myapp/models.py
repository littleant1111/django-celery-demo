#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class USER(models.Model):
    user = models.CharField(u'用户名测试', max_length=20)
    passwd = models.CharField(u'用户名密码', max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' % (self.user)
    class Meta:
        verbose_name = u'我的测试用户表'
        verbose_name_plural =  u'我的测试用户表'