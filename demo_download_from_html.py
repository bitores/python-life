# -*- coding: cp936 -*-
import os
import re
import urllib
import urllib2
import requests
import htmllib
import formatter

"""
download the resource
"""

packages = [
    "biu_爱心_0725_170",
    "街密_商店_0730_199",
    "街蜜_圣诞186_239",
    "橘子娱乐_放映机_0725_163",
    "卷皮_大圣归来298_296_306",
    "卷皮_小车_296_297",
    "觅食_礼到了243_246",
    "觅食_美女食神_189_192",
    "觅食_烹饪_0725_167",
    "球球连萌_老虎机211_247",
    "土豪赢三张_超级马里奥224_295",
    "想去_3D飞机_0728_172",
    "想去_宝丽来相机_263",
    "想去_邮箱_法式浪漫_206",
    "想去_唱片机244_250_261",
    "想去_193_197",
    "完美壁纸_3D水族馆_271",
    "香蕉段子_骗吃骗喝_283",
    "20150605_范冰冰"
]


def getHtmlByUrl2(url):
    req=urllib2.Request(url)
    page=urllib2.urlopen(req)
    content=page.read()
    


def getHtmlByUrl(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getLinkByHTML(html):
    
    # print html
    start=html.find('http')
    end=html.find('zip')
    #print start, end
    return html[start:end+3]

def getLinkByHTML2(html):
    format = formatter.AbstractFormatter(formatter.NullWriter())
    ptext = htmllib.HTMLParser(format)
    ptext.feed(html)
    for link in ptext.anchorlist:
       print(link)
       return link
    return ""

    
def getLinkByPackageName(package_name):
    params=package_name.decode('gbk','replace')
    params = urllib.quote(params.encode('utf-8','replace'))
    url= "http://3dbizhi.com/tool/cell/cell_get.php?name=%s" % params
    html = getHtmlByUrl(url)
    #link = getLinkByHTML2(html)
    link = getLinkByHTML(html)
    return link


def urlcallback(a,b,c):
    """
        call back function
        a,已下载的数据块
        b,数据块的大小
        c,远程文件的大小
    """
    print "callback"
    prec=100.0*a*b/c
    if 100 < prec:
        prec=100
    print "%.2f%%"%(prec,)
def download(base_url):
    filename=os.path.basename(base_url)
    #print filename
    #本地
    localFile = os.path.join('E:\Download_packages',filename)#+文件名 
    #线上
    remoteFile = base_url

    print "downloading with urllib"
    urllib.urlretrieve(remoteFile, localFile,urlcallback)

    print "downloading with urllib2"
    f = urllib2.urlopen(remoteFile) 
    with open(localFile, "wb") as code:
         code.write(f.read())   
    print "downloading with requests"
    r = requests.get(remoteFile) 
    with open(localFile, "wb") as code:
         code.write(r.content)



def getZip():
    for name in packages:
        link = getLinkByPackageName(name)
        print link
        if link:
            download(link)
        else:
            print name+"没有找到"
        # download zip
        #socket.setdefaulttimeout(10)


if __name__ == '__main__':
    getZip()
