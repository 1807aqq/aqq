from django.db import models

class User(models.Model):
    # 用户ID
    uid = models.IntegerField(primary_key=True, unique=True, null=False)
    # 用户手机号码
    phone = models.IntegerField(null=False)
    # 用户密码
    passwd = models.CharField(max_length=50,null=False)
    # 用户姓名
    name = models.CharField(max_length=50,null=False)
    # 用户地址
    address = models.CharField(max_length=200, null=False)
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
    em_contact = models.IntegerField(null=False)

    class Meta:
        db_table = 'user'


class Loan(models.Model):
    id = models.IntegerField(primary_key=True)
    # 用户ID
    uid = models.IntegerField()
    # 借贷金额
    amount = models.FloatField()
    # 借贷标题
    title = models.CharField(max_length=100)
    # 客户类别
    cus_type = models.CharField(max_length=10)
    # 居住时间
    time_period = models.CharField(max_length=10)
    # 贷款期限
    time_limit = models.IntegerField()
    # 借款机构
    instotution =models.CharField(max_length=50)
    # 还款方式 -- 0: 先息后本 1:先本后息
    payment = models.IntegerField()
    # 居住城市
    city = models.CharField(max_length=10)
    # 工作年限
    work_time = models.IntegerField()
    # 税后工资
    salary_after_tax = models.FloatField()
    # 借款目的
    purpose = models.TextField()
    # 借款描述
    info = models.TextField()

    class Meta:
        db_table = 'loan'