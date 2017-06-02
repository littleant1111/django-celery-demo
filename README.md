1、安装如下组件：
pip install Celery
pip install django-celery
pip install celery-with-redis
pip install djangorestframework
pip install paramiko
#pip install ansible==2.2.2
pip install supervisor
pip install redis
pip install MySQL-python
pip install DBUtils

Django 版本：
>>> print django.VERSION
(1, 11, 0, u'alpha', 0)
测试通过


2、安装redis，并且配置好
安装略，配置：
vim /etc/redis/6379.conf
# bind 127.0.0.1
protected-mode no
daemonize yes
启动：
# ./redis-server /etc/redis/6379.conf

3、配置Celery异步任务系统
vim /etc/supervisord.conf
最后添加
[program:celery-worker]
command=/usr/bin/python manage.py celery worker --loglevel=info -E -c 2
directory=/yourpath/testcelery
stdout_logfile=/var/log/celery-worker.log
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=QUIT
numprocs=1
启动celery
/usr/local/bin/supervisord -c /etc/supervisord.conf
supervisorctl status



4、配置数据库并且运行：
settings.py 中的 DATABASES 参数配置
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver 0.0.0.0:8002

5、访问地址
http://youdomain_or_ipaddress:8002/myapp/firstInterface/
前端很快返回。注意查看下 supervisor 日志：
tail -22f /var/log/celery-worker.log

6、等待30s，查看数据库表中
有两条记录如下：
10	zhangsan	123456x	2017-06-02 06:07:49.591973
11	zhangsan	123456x	2017-06-02 06:08:21.765372











