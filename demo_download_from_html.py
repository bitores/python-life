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
    "biu_����_0725_170",
    "����_�̵�_0730_199",
    "����_ʥ��186_239",
    "��������_��ӳ��_0725_163",
    "��Ƥ_��ʥ����298_296_306",
    "��Ƥ_С��_296_297",
    "��ʳ_����243_246",
    "��ʳ_��Ůʳ��_189_192",
    "��ʳ_���_0725_167",
    "��������_�ϻ���211_247",
    "����Ӯ����_���������224_295",
    "��ȥ_3D�ɻ�_0728_172",
    "��ȥ_���������_263",
    "��ȥ_����_��ʽ����_206",
    "��ȥ_��Ƭ��244_250_261",
    "��ȥ_193_197",
    "������ֽ_3Dˮ���_271",
    "�㽶����_ƭ��ƭ��_283",
    "20150605_������"
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
        a,�����ص����ݿ�
        b,���ݿ�Ĵ�С
        c,Զ���ļ��Ĵ�С
    """
    print "callback"
    prec=100.0*a*b/c
    if 100 < prec:
        prec=100
    print "%.2f%%"%(prec,)
def download(base_url):
    filename=os.path.basename(base_url)
    #print filename
    #����
    localFile = os.path.join('E:\Download_packages',filename)#+�ļ��� 
    #����
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
            print name+"û���ҵ�"
        # download zip
        #socket.setdefaulttimeout(10)


if __name__ == '__main__':
    getZip()
