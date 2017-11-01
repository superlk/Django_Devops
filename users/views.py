# coding:utf-8
from django.shortcuts import render
from users.models import *
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

import json
# Create your views here.

# 主页
def index(request):
    return render(request,'index.html',)


# 注册页
def reg(request):
    if request.method=='POST':
       username=request.POST['username']
       name=request.POST['name']
       password=request.POST['password']
       phone=request.POST['phone']
       email=request.POST['email']
       role=request.POST['role']
       status=request.POST['status']
       data={'username':username,'name':name,'password':password,'phone':phone,'email':email,'role':role,'status':status}
       obj=UserModel.objects.create(**data)
       obj.save()
       result ={'code':0,'msg':'insert ok'}
       return JsonResponse(result,safe=False)
    #data=UserModel.objects.all().values()
    #if request.method=='POST':
    return render(request,'reg.html',)

# 登录
def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       data={'username':username}
       res=UserModel.objects.filter(**data).values()
       if username==res[0]['username'] and password==res[0]['password']:
           result={'code':0,'msg':res[0]}
           request.session['username']=username
           request.session['role']=res[0]['role']
           print '---session---',request.session['username']
       else:
           result={'code':1,'msg':'username or password is error'}
       return JsonResponse(result,safe=False)
    return render(request,'login.html',)

# 用户主页
def user(request):
    if not request.session.has_key('username'):
        return HttpResponseRedirect("/user//")
    else:
       print '---user_session---',request.session['username']
       data={}
       data['username']=request.session['username']
       result=UserModel.objects.filter(**data).values()
       rest={}
       rest['username']=request.session['username']
       rest['role']=int(request.session['role'])
       print '--rest-',rest
       print '--res[0]-',result[0]
       return render(request,'list.html',{'res':rest,'result':result[0]})


# 用户列表
def userlist(request):
    if not request.session.has_key('username'):
        return HttpResponseRedirect('/user//')
    else:
        data=UserModel.objects.all().values()
        print "____userlist____data__",data
        return render(request,'userlist.html',{'res':request.session,'result':data})

# 增加用户
def add(request):
    if not request.session.has_key('username'):
        return HttpResponseRedirect('/user//')
    if request.method=='POST':
       username=request.POST['username']
       name=request.POST['name']
       password=request.POST['password']
       phone=request.POST['phone']
       email=request.POST['email']
       role=request.POST['role']
       status=request.POST['status']
       data={'username':username,'name':name,'password':password,'phone':phone,'email':email,'role':role,'status':status}
       obj=UserModel.objects.create(**data)
       obj.save()
       result ={'code':0,'msg':'insert ok'}
       return JsonResponse(result,safe=False)

# 删除用户
def delete(request):
    if not request.session.has_key('username'):
        return HttpResponseRedirect('/user//')
    uid=request.GET['id']
    print '--uid--',uid 
    data=UserModel.objects.get(id=uid).delete()
    #data.save()       
    result ={'code':0,'msg':'delete ok'}
    return JsonResponse(result,safe=False)

# 编辑用户
def userinfo(request):
    if not request.session.has_key('username'):
        return HttpResponseRedirect('/user//')
    uid=request.GET['id']
    data=UserModel.objects.filter(id=uid).values()
    print '---userinfo_data-',data
    return JsonResponse(data[0],safe=False)

# 更新
def update(request):
    if not request.session.has_key('username'):
          return HttpResponseRedircet('/user//')
    if request.method=='POST':
       uid=request.POST['id']
       username=request.POST['username']
       name=request.POST['name']
       password=request.POST['password']
       phone=request.POST['phone']
       email=request.POST['email']
       role=request.POST['role']
       status=request.POST['status']
       data={'username':username,'name':name,'password':password,'phone':phone,'email':email,'role':role,'status':status}
       obj=UserModel.objects.filter(id=uid).update(**data)
       result ={'code':0,'msg':'update is ok'}
       return JsonResponse(result,safe=False)


# 用户登出
def logout(request):
    request.session.clear()
    return HttpResponseRedirect("/user//")
