# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import models
from django.contrib import auth

# Create your views here.

#首页
def index(request):
    
    bbs_list=models.bbs.objects.all()
    #print bbs_list
    return render_to_response('index.html',{'bbs_list':bbs_list,'user':request.user})


#
def bbs_detail(request,bbs_id):
    bbs=models.bbs.objects.get(id=bbs_id)
    print "---------",type(bbs)
    return render_to_response('bbs_detail.html',{'bbs_obj':bbs})

# 等出
def logout_view(request):
    user=request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b>logout<br/><a href='/'> Re-login </a>"%user)    

# 发帖
def bbs_pub(request):
    return render_to_response('bbs_pub.html',{'user':request.user})

# 写入
def bbs_sub(request):
    content=request.POST.get('content')
    print "===>",content
    author=models.bbs_user.objects.get(user__username=request.user)
    #author=models.bbs_user.objects.get(user__username="root")
    models.bbs.objects.create(
       title="test",
       summary="HAHA",
       content=content,
       author=author,
       view_ciunt=1,
       ranking=1, 
       )
    return HttpResponse('yes')
