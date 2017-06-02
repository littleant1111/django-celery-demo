#!/usr/bin/python
# -*- coding: UTF-8 -*-


from celery import task
from models import USER


@task
def test(user, passwd):
    import time
    time.sleep(30)
    try:
        ret_user = USER.objects.create(user=user, passwd=passwd)
        return True
    except Exception,e:
        print "exceptions: ", e
        return False


