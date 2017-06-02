from django.shortcuts import render

# Create your views here.

from tasks import *
from django.shortcuts import render,render_to_response
from django.http import JsonResponse
from models import USER


def firstInterface(request):
    # if request.method == 'GET':
    #     return render(request, 'test.html', {'data':'test-----data'})
    # elif request.method == 'POST':
        # id = request.GET.get('id')
    # user = request.POST.get('user')
    # passwd = request.POST.get('passwd')
    user = 'zhangsan'
    passwd = '123456x'
    USER.objects.create(user=user, passwd=passwd)
    test.delay(user, passwd)
    return JsonResponse('ok', safe=False)