# -*- coding: cp936 -*-
import re
import string

s = "    mary had a little         lamb   "
print s

if re.search("m",s):print "Match!-m" #char literal
if re.search("[@A-Z]",s):print "Match!-[@A-Z]" #char class
if re.search("d",s):print "Match!-d" #digits class


#=============== 数组拼接 ============
L = string.split(s)
print L
L2 = string.join(L,"-")
print L2



#========================= 字符串截取 =============
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s",text)
if m:
    print m.group(0), '\n',m.group(1)
else:
    print 'not match'
    
m=re.match("(\d+)\.(\d+)","23.123")
print m.groups(),m.group(1),m.group(2)
