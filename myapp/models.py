from django.db import models

class User(models.Model):
    # 用户ID
    uid = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    # 用户手机号码
    phone = models.CharField(max_length=11,null=False)
    # 用户密码
    passwd = models.CharField(max_length=50,null=False)
    # 用户姓名
    name = models.CharField(max_length=50,null=False)
    # 用户昵称
    nickname = models.CharField(max_length=50, null=False)
    # 用户身份证
    identity = models.CharField(max_length=30)
    # 用户银行卡号
    bank_num = models.CharField(max_length=50)
    # 用户银行名称
    banks = models.CharField(max_length=50)
    # 用户所在地
    city = models.CharField(max_length=30)
    # 用户开户行
    open_bank = models.CharField(max_length=50)
    # 用户地址
    address = models.CharField(max_length=200,blank=True,null=True)
    # 教育信息
    edu = models.CharField(max_length=50,blank=True,null=True)
    # 毕业学校
    school = models.CharField(max_length=30,blank=True,null=True)
    # 婚姻状态
    marriage = models.CharField(max_length=10,blank=True,null=True)
    # 公司信息
    company = models.CharField(max_length=50,blank=True,null=True)
    # 工资
    salary = models.IntegerField(blank=True,null=True)
    # 是否买房
    home = models.BooleanField(blank=True,null=True)
    # 是否买车
    car = models.BooleanField(blank=True,null=True)
    # 已修改----账户余额
    em_contact = models.CharField(max_length=30,blank=True,null=True)

    class Meta:
        db_table = 'user'

#借贷表
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

class Institutions(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    name = models.CharField(max_length=50)
    info = models.TextField()
    class Meta:
        db_table = 'institutions'


class Product(models.Model):
    # 产品id
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True, null=False)
    # 产品名称
    name = models.CharField(max_length=50)
    # 产品类型
    type = models.IntegerField()
    # 年收益率/利息
    y_rate = models.FloatField()
    # 投资周期/借款多长时间
    time_limit = models.IntegerField()
    # 融资金额/
    amount = models.FloatField()
    # 机构id
    institution = models.ForeignKey(Institutions,on_delete=models.CASCADE,related_name='pro')
    # 风险级别
    risk = models.FloatField()
    # 还款方式
    payment = models.IntegerField()
    # 项目简介
    info = models.TextField()

    class Meta:
        db_table = 'products'


# 资金记录表
class Money(models.Model):
    # 记录id
    id = models.IntegerField(null=False, primary_key=True, unique=True)
    # 获取当前时间  设置settings USE_TZ=False
    time = models.DateTimeField(auto_now_add=True)
    # 用户id
    uid = models.IntegerField(null=False)
    # 资金来往类型  体现， 充值
    type = models.CharField(max_length=20)
    # 金额
    amount = models.FloatField(null=False)
    # 状态  0 正在进行   1 为已完成
    status = models.IntegerField(null=False)

    class Meta:
        db_table = 'money'


# 行业动态表


class Industry(models.Model):
    ip = models.IntegerField(primary_key=True, auto_created=True, null=False, unique=True)
    # 动态标题
    name = models.CharField(max_length=100, null=False)
    # 新闻发布时间
    time = models.CharField(max_length=50)
    # 新闻详情
    info = models.TextField()
    class Meta:
        db_table = 'industries'


# 投资记录表

class Investment(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    # 用户id
    uid = models.IntegerField(null=False)
    # 产品id
    pid = models.IntegerField(null=False)
    # 投资金额
    amount = models.FloatField()


    class Meta:
        db_table = 'investment'

