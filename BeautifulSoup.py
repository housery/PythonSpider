# -*- coding:utf-8 -*-
# 利用Beautifulsoup获取网页节点，爬取豆瓣书店的图片
import urllib
from bs4 import BeautifulSoup

#解析网页
def get_content(url):
    html = urllib.urlopen(url)
    content = html.read()
    html.close()

    return content
# 获取图片
def get_img(content):
    soup = BeautifulSoup(content,"html.parser")
    carousel = soup.find(class_ ="carousel")         //carousel为豆瓣网站的一个div节点
    imgs = carousel.find_all("img")

    x = 1
    for img in imgs:
        print img['src']
        image_name = "%s.jpg" % x

        urllib.urlretrieve(img['src'] , image_name)
        x+=1

url = "https://book.douban.com/"
content = get_content(url)
get_img(content)
