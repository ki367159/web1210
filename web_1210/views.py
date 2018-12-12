from django.http import HttpResponse
from django.shortcuts import render

def root(request):
    name = request.GET.get('name', 'guest')
    return HttpResponse('Hi, {}'.format(name))

def hello(request, name):
    return HttpResponse('Hi, {}'.format(name))

def s(request, number):
    return HttpResponse(number ** 2)

def l(request, number1, number2):
    # if number1 > number2:           #方法一
    #     _list = reversed(range(number2, number1+1))
    # else:
    #     _list = range(number1, number2+1)

    step = -1 if number1 > number2 else 1  #方法二
    _list = range(number1, number2+step, step)

    return render(request, 'l.html', {'list': _list})