# -*- coding: cp936 -*-
import sys
import os

abspath=os.path.abspath(sys.argv[0])
(filepath,filename)=os.path.split(abspath)
(basename,filesuffix)=os.path.splitext(filename)
print "脚本名：", filename
print "文件名：", basename
print "文件后缀：", filesuffix
print "脚本当前目录：", filepath#os.path.dirname(abspath)
print "脚本当前完整路径：", abspath


for i in range(1, len(sys.argv)):

    print "参数", i, sys.argv[i]
