from django.contrib import admin
from .models import Category,Course
# Register your models here.

admin.site.site_header = 'CSDN微课后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name']
   search_fields = ['name']
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'courseName', 'filname', 'imgname', 'pCategory', 'price', 'summary', 'status',
                    'creatDatetime']
    list_filter = ['courseName','creatDatetime']
    search_fields = ['courseName','creatDatetime']
    filter_horizontal = ['userBuyer','userShoppingcart']
