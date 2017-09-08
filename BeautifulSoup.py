# -*- coding:utf-8 -*-
# Beautifulsoup tag name class attributes
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
    carousel = soup.find(class_ ="carousel")
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