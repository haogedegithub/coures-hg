from django.db import models
import datetime
from user.models import User
import os
# Create your models here.
#课程种类
class Category(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '课程种类表'
    name = models.CharField(max_length = 50,unique = True,verbose_name = '课程种类')
    def __str__(self):
        return self.name
#将文件保存到数据库，及对应文件夹下
def save_file(instance,filename):
    return os.path.join('video',filename)
def save_img(instance,filenname):
    return os.path.join('static','img',filenname)
class Course(models.Model):
    def __str__(self):
        return self.courseName
    class Meta():
        verbose_name = verbose_name_plural = '课程表'
    courseName = models.CharField(max_length = 40,verbose_name = '课程名称')
    filname = models.FileField(upload_to = save_file,verbose_name = '文件名称')
    imgname = models.ImageField(upload_to = save_img,verbose_name = '课程图片')
    pCategory = models.ForeignKey(to = Category,related_name = 'course_set',on_delete = models.CASCADE,verbose_name = '课程分类')
    price = models.DecimalField(max_digits = 7,decimal_places = 2,default = 0,verbose_name = '课程价格')
    summary = models.CharField(max_length = 500,default = '',verbose_name = '课程介绍',blank =  True)
    # 0免费，1收费
    status = models.PositiveSmallIntegerField(default = 0,verbose_name = '状态',choices = ((0,'免费'),(1,'收费')))
    creatDatetime = models.DateTimeField(default = datetime.datetime.now(),verbose_name = '创建时间',blank = True)
    userBuyer = models.ManyToManyField(to = User,related_name = 'userBuyer_set',verbose_name = '购买用户',blank = True)
    userShoppingcart = models.ManyToManyField(to = User,related_name = 'userShoppingcart_set',verbose_name = '加入购物车的用户',blank = True)