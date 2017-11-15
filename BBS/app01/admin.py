from django.contrib import admin
from app01 import models
# Register your models here.

class bbs_admin(admin.ModelAdmin):
    list_display=('title','summary','author','signature','view_ciunt','created_at')
    list_filter=('created_at',)
    search_fields=('title','author__user__username')
    
    def signature(self,obj):
        return obj.author.signature
    signature.short_description="wooooo"

admin.site.register(models.bbs,bbs_admin)
admin.site.register(models.category)
admin.site.register(models.bbs_user)
#admin.site.register(models.django_comments)
