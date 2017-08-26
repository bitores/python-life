# -*- coding: cp936 -*-
from twisted.web.client import getPage
from twisted.internet import reactor
"""
pip install twisted
"""

links = [ 'http://www.verycd.com/topics/%d/'%i for i in range(5420,5430) ]
 
def parse_page(data,url):
    print len(data),url
 
def fetch_error(error,url):
    print error.getErrorMessage(),url
 
# ����ץȡ����
for url in links:
    #�ɹ������parse_page����
    getPage(url,timeout=5).addCallback(parse_page,url).addErrback(fetch_error,url)     #ʧ�������fetch_error����
 
reactor.callLater(5, reactor.stop) #5���Ӻ�֪ͨreactor��������
reactor.run()
