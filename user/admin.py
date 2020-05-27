from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','account','password','username','money','gender','tel']
    #过滤器
    list_filter = ['account']
    #搜索
    search_fields = ['gender']