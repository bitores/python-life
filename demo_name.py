# -*- coding: cp936 -*-
#！E:/python_worspace
#Filename:demo_name.py
#一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序不执行，
#我们可以用__name__属性来使该程序志仅在该模块自身运行时执行。

print __name__

if __name__=='__main__':
    print '程序自身在运行'
else:
    print '我来自另一个模块'
