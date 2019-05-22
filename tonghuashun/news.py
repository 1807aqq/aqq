import re
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree
from aqq_1.tools import headers
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
    for url in items:
        #print(url)
        data = []
        root = requests.get(url,headers = headers.get_headers())
        text = root.text
        time.sleep(2)
        # filename = url.split('/')[-1]
        # with open(filename, 'w') as f:
        #     f.write(text)
        dt = {}
        try:
            dt['info'] = re.findall(r'<div class="main-text atc-content">(.*?)<p class="bottomSign"', text, re.S)[0].strip()
            dt['news_time'] = re.findall(r' id="pubtime_baidu">(.*?)</span>', text)[0]
            dt['title'] = re.findall(r'<title>(.*?)</title>', text)[0]
            data.append(dt)
        except:
            pass




if __name__ == '__main__':
    url = 'http://www.10jqka.com.cn/'
    # now_time = datetime.datetime.now().strftime('%H-%M-%S')
    # now_time = time.localtime().tm_min
    # if now_time % 10 == 0:
    #     print(now_time)
    Downlode(url)

