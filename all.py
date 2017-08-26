#coding=gb2312

import time
import datetime
import calendar

i=raw_input('please input a number:')
print 'you just input a number:' + i

del i
print 'when you del the number container,and you woldnot get it again.'

print '朋友，一起走'

str="http://www.baidu.com/"


print str
print str[0]
print str[2:5]
print str[2:]
print str*2


tinydict={'name':'zhengjie','lname':'jie','Firstname':'Huang'}

print tinydict.keys()
print tinydict.values()

p = list(tinydict)
q = tuple(tinydict)

print p,q

if 'name' in tinydict:print 'name'
else: print "your name"


if p is q: print 'p is q'
else: print 'p is not q'

for le in str:
    if le == '/':
        pass
        print 'end for'
    print le

print time.time()
print time.localtime(time.time())
print time.strftime("%Y",time.localtime(time.time()))


for i in range(1,13):
    cal = calendar.month(2016,i)
    print ' 月份'
    print cal
print cal
