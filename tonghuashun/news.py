import re
import time
import pymysql
import requests
from bs4 import BeautifulSoup
from lxml import etree
from tools import headers

import base64

msg = {
        'host':'10.12.152.206',
        'port':3306,
        'user':'root',
        'password':'qwl123',
        'db':'aqq',
        'charset':'utf8'
}
conn = pymysql.Connect(**msg)
cursor = conn.cursor()
def Downlode():
    url = 'http://www.10jqka.com.cn/'
    resp = requests.get(url)
    html = resp.content
    prams(html)


def prams(html):
    #soup = BeautifulSoup(html, 'lxml')
    root = etree.HTML(html)
    # messages = soup.find_all('ul','tab-container')
    messages = root.xpath("//div[@class='box ssrmtab']//a")[1:]
    links = []
    for message in messages:
        url = message.get('href')
        if str(url).startswith('http://field.10jqka.com.cn') or \
                str(url).startswith('http://stock.10jqka.com.cn'):
            links.append(url)
    save(links)

def save(items):
    data = []
    id_= 1
    cursor.execute('truncate table industries')
    conn.commit()
    for url in items:
        #print(url)
        root = requests.get(url,headers = headers.get_headers())
        text = root.text
        time.sleep(1)
        # filename = url.split('/')[-1]
        # with open(filename, 'w') as f:
        #     f.write(text)
        try:
            info = re.findall(r'<div class="main-text atc-content">(.*?)<p class="bottomSign"', text, re.S)[0].strip()
            base64_info = base64.b16encode(info.encode()).decode()
            # base64 进行编码

            news_time= re.findall(r' id="pubtime_baidu">(.*?)</span>', text)[0]
            title= re.findall(r'<title>(.*?)</title>', text)[0]

            print(info)
            sql = 'insert into industries(ip, name,time,info)values(%s,"%s","%s","%s")'%(id_, title,news_time,base64_info)
            cursor.execute(sql)

            id_ += 1
            print('插入成功')
        except Exception as e:
            print('插入失败',e)
            conn.rollback()

    conn.commit()


def read_data():
    cursor.execute('select * from industries')
    for row in cursor.fetchall():
        print(base64.b16decode(row[3].encode()).decode())


if __name__ == '__main__':

    # now_time = datetime.datetime.now().strftime('%H-%M-%S')
    # now_time = time.localtime().tm_min
    # if now_time % 10 == 0:
    #     print(now_time)
    Downlode()
    #read_data()  # 测试

