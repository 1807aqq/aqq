import re
import time
import pymysql
import requests
from bs4 import BeautifulSoup
from lxml import etree
from tools import headers
msg = {
        'host':'10.12.152.85',
        'port':3306,
        'user':'root',
        'password':'0314',
        'db':'aqq',
        'charset':'utf8'
}
conn = pymysql.Connect(**msg)
cursor = conn.cursor()
def Downlode(url):
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
            news_time= re.findall(r' id="pubtime_baidu">(.*?)</span>', text)[0]
            title= re.findall(r'<title>(.*?)</title>', text)[0]
            # cursor.execute('truncate table industries')
            # conn.commit()
            print(info)
            sql = 'insert into industries(name,tiem,info)values(%s,%s,%s)'%(title,news_time,info)
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print('插入失败',e)
            conn.rollback()





if __name__ == '__main__':
    url = 'http://www.10jqka.com.cn/'
    # now_time = datetime.datetime.now().strftime('%H-%M-%S')
    # now_time = time.localtime().tm_min
    # if now_time % 10 == 0:
    #     print(now_time)
    Downlode(url)

