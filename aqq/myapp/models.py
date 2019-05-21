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



class Product(models.Model):
    # 产品id
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    # 产品名称
    name = models.CharField(max_length=50, null=False)
    # 产品类型   # 是借贷类（1）和投资类（2）
    type = models.IntegerField(null=False)
    # 年收益率/利息
    y_rate = models.FloatField(null=False)
    # 投资周期/借款多长时间
    time_limit = models.IntegerField(null=False)
    # 融资金额/
    amount = models.FloatField(null=False)

    class Meta:
        db_table = 'products'


# 资金记录表
class money(models.Model):
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

class industry(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    # 动态标题
    name = models.CharField(max_length=100, null=False)
    # 新闻链接
    url = models.CharField(max_length=300)

    class Meta:
        db_table = 'industries'


# 投资记录表

class investment(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    # 用户id
    uid = models.IntegerField(null=False)
    # 产品id
    pid = models.IntegerField(null=False)
    # 投资金额
    amount = models.FloatField()


    class Meta:
        db_table = 'investment'

