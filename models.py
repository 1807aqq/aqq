from django.db import models

class User(models.Model):
    # 用户ID
    uid = models.IntegerField(primary_key=True, unique=True, null=False)
    # 用户手机号码
    phone = models.IntegerField(null=False)
    # 用户密码
    passwd = models.CharField(max_length=50)
    # 用户姓名
    name = models.CharField(max_length=50,null=False)
    # 用户地址
    address = models.CharField(max_length=200)
    # 教育信息
    edu = models.CharField(max_length=50)
    # 毕业学校
    school = models.CharField(max_length=30)
    # 婚姻状态
    marriage = models.CharField(max_length=10)
    # 公司信息
    company = models.CharField(max_length=50)
    # 工资
    salary = models.IntegerField()
    # 是否买房
    home = models.BooleanField()
    # 是否买车
    car = models.BooleanField()
    # 紧急联系人电话
    em_contact = models.IntegerField()