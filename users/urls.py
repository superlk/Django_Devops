from django.conf.urls import include ,url

from . import views


urlpatterns=[
      #url(r'^hello/$',views.hello),
      url(r'^reg/$',views.reg),
      url(r'^login/$',views.login),
      url(r'^user/$',views.user),
      url(r'^logout/$',views.logout),
      url(r'^userlist/$',views.userlist),
      url(r'^add/$',views.add),
      url(r'^delete/$',views.delete),
      url(r'^userinfo/$',views.userinfo),
      url(r'^update/$',views.update),
      url(r'^/$',views.index),

]
