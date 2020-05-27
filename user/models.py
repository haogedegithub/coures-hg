from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '用户表'
    def __str__(self):
        return self.account
    account = models.CharField(max_length = 16,unique = True,verbose_name = '账号')
    password = models.CharField(max_length = 16,verbose_name = '密码')
    username = models.CharField(max_length = 16,verbose_name = '用户名',blank = True)
    #总位数为12，小数位为2，默认为0
    money = models.DecimalField(max_digits = 12,decimal_places = 2,default = 0,verbose_name = '余额')
    #1男，0女
    gender = models.PositiveSmallIntegerField(default = 0,verbose_name = '性别',choices = ((0,'女'),(1,'男')))
    tel = models.CharField(max_length = 11,default = '',verbose_name = '电话',blank = True)