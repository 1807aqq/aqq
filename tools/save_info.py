import random


# 抵押贷款保存信息
from myapp.models import Investment, Product


def get_info(request):
    amount = request.POST.get('amount')
    title = request.POST.get('title')
    customertype = request.POST.get('customertype')
    livetime = request.POST.get('livetime')
    period = request.POST.get('period')
    lenders = request.POST.get('lenders')
    lendmethod = request.POST.get('lendmethod')
    livespace = request.POST.get('livespace')
    workertime = request.POST.get('workertime')
    salary = request.POST.get('salary')
    info = request.POST.get('info')
    use = request.POST.get('use')
    files = request.FILES.get('files')
    return (amount,title,customertype,livetime,period,lenders,lendmethod,livespace,workertime,salary,info,use)

def mortgage_save(loan,product,user,amount, title, customertype, livetime, period, lenders, lendmethod, livespace,
                  workertime, salary,info, use,type):
    # 保存借贷信息表
    # 插入借贷表
    loan.uid = user.uid
    loan.amount = amount
    loan.title = title
    loan.cus_type = customertype
    loan.time_period = livetime
    loan.time_limit = period
    loan.instotution = lenders
    loan.payment = lendmethod
    loan.city = livespace
    loan.work_time = workertime
    loan.salary_after_tax = salary
    loan.purpose = use
    loan.info = info
    loan.save()
    # 同时生成一个产品表
    # 一个产品的id为一个借贷的id
    product.id = loan.id
    product.name = title
    product.type = type
    dic = {24: 10.3, 36: 12.7, 48: 14}
    product.y_rate = dic[int(period)]
    product.time_limit = period
    product.amount = int(amount) / 10000
    product.risk = random.choice([3.5, 4.5, 4, 3])
    product.payment = lendmethod
    product.institution_id = lenders
    product.info = info
    product.save()

# 查询用户投资产品

def user_product(user,Product,Investment):
    log_inves = Investment.objects.filter(uid=user.uid)
    class A(object):
        pass
    logs = []
    pay = ['先息后本', '先本后息', '等额本金', '等额本息']
    for i in log_inves:
        # 查询用户每个投资记录的年利率然后计算收益
        products = Product.objects.filter(id=i.pid)
        for j in products:
            a = A()
            # 产品名称
            a.title = j.name
            # 还款方式
            a.payment = pay[j.payment-1]
            # 期限
            a.limit=j.time_limit
            # 利率
            a.rate = j.y_rate
            logs.append(a)
    return logs
    # 资产总额




