#!/usr/bin/python
# -*- coding: UTF-8 -*-


from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^firstInterface/', firstInterface, name='firstInterface'),
]