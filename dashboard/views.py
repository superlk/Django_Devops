#coding;utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#def hello(request):
#    #return HttpResponse('<h1>hello world </h1>')
#    return render(request,'index.html',{'name':'lk','age':'18'})

def idc(request):
    return HttpResponse('<h1>hello idccccccc </h1>')

def server(request):
    return HttpResponse('<h1>hello serverrrrrrrrrr </h1>')

def index(request):
    return render(request,'index.html',)
