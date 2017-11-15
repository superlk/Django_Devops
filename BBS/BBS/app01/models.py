# coding:utf-8
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

from __future__ import unicode_literals

from django.db import models

# 导入django用户表
from django.contrib.auth.models import User

# Create your models here.

# 帖子
class bbs(models.Model):
     # 题目
     title=models.CharField(max_length=64)
     # 表里可以为空null=true，django——admin里可以为空blank=true
     summary=models.CharField(max_length=256,blank=True,null=True)
     # 内容
     content=models.TextField()
     # 作者外键bbs_user
     author=models.ForeignKey('bbs_user')
     # 评论数，
     view_ciunt=models.IntegerField()
     # 排名
     ranking=models.IntegerField()
     # 创建日期
     created_at=models.DateTimeField(auto_now=True)
     # 修改日期
     update_at=models.DateTimeField(auto_now=True)
     # 不写这个，用命令行查看会返回内存地址无法辨认，写上会返回指定的
     def __unicode__(self):
        return self.title   
  
     
# 评论 django 自带评论系统
#class comments(models.Model):
#     pass

# 板块
class category(models.Model):
      # 模块名，unique=true ,在表里唯一，但是不主键
      name=models.CharField(max_length=32,unique=True)
      # 版主
      administrator=models.ForeignKey('bbs_user')
     

# 用户,继承用django自带的用户系统
class bbs_user(models.Model):
      #外键onetoone 一对一，ForeignKey一对多(不能反向查)，
      user=models.OneToOneField(User)
      # 签名
      signature=models.CharField(max_length=128,default='ci chu sheng lue')
      # 头像 ，图片字段，会自动在根目录下创建upload_imgs目录，图片传到这里，不穿默认用user-1.jpg
      photo=models.ImageField(upload_to="upload_imgs/",default="uplpoad_imgs/user-1.jpg")
      
      def __unicode__(self):
          return self.user.username 


