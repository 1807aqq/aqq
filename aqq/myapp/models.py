from django.db import models


# Create your models here.


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
