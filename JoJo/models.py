from django.db import models

# Create your models here.
class User(models.Model):
    # 基本信息
    username = models.CharField(max_length=50)                  #用户名也就是账号
    password = models.CharField(max_length=50)                  #密码
    nickname = models.CharField(max_length=20,default='Tom')    #昵称
    level = models.CharField(max_length=20, default='大不自多')  #等级
    gender =  models.CharField(max_length=5, default='',null=True,blank=True)        #性别
    target = models.CharField(max_length=50, default='',null=True,blank=True)        #目标
    coin =  models.IntegerField(default=0)                      #金币
    wordbook = models.CharField(max_length=20, default='GRE')   #单词书
    email = models.CharField(max_length=30, default='')


    # 动态信息
    word_num_today = models.IntegerField(default=0)             #今日单词数量
    word_num_remember = models.IntegerField(default=0)          #已经记忆
    day_signup = models.IntegerField(default=0)                 #累计打卡

    word_total_remember = models.CharField(max_length=20000,default='',null=True,blank=True)
    word_total_plan = models.CharField(max_length=20000,default='',null=True,blank=True)
    record = models.CharField(max_length=20000,default='',null=True,blank=True)





class Word(models.Model):
    wordname    =  models.CharField(max_length=50, primary_key=True)
    group       =  models.CharField(max_length=20)
    soundmark   =  models.CharField(max_length=50, null=True,blank=True)
    explanation =  models.CharField(max_length=200, null=True,blank=True)
    demo_1      =  models.CharField(max_length=100, null=True,blank=True)
    demo_1_translate = models.CharField(max_length=100, null=True, blank=True)
    demo_2      =  models.CharField(max_length=100, null=True,blank=True)
    demo_2_translate = models.CharField(max_length=100, null=True, blank=True)
    demo_3      =  models.CharField(max_length=100, null=True,blank=True)
    demo_3_translate = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.wordname