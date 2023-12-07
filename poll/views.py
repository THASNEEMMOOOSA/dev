from django.shortcuts import render,loader
from django.http import HttpResponse
from .models import Userinfo
from django.db.models import Q


# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello World</h1>')

def h(request):
    return HttpResponse('<h1>Helooooooooooooooooooooooooooooooooo <u>Universeeeee</u></h1>')

def datas(request):
    d=Userinfo.objects.all()
    template=loader.get_template('index.html')
    context={
        'd':d,
    }
    return HttpResponse(template.render(context,request))
def detailed(request,id):
    d=Userinfo.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'd':d,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())


def test(request):
    g=Userinfo.objects.all().order_by('-id').values()
    template=loader.get_template('template.html')
    context={
        'fn':g,
    }
    return HttpResponse(template.render(context,request))






