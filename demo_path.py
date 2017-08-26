# -*- coding: cp936 -*-
#！E:python_worspace
#Filename:demo01.py
import sys

print('命令行参数如下')
for i in sys.argv:
      print '参数：',i
      print '\n'

print '\n\n The PYTHONPATH is',sys.path,'\n'
