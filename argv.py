# -*- coding: cp936 -*-
import sys
import os

abspath=os.path.abspath(sys.argv[0])
(filepath,filename)=os.path.split(abspath)
(basename,filesuffix)=os.path.splitext(filename)
print "�ű�����", filename
print "�ļ�����", basename
print "�ļ���׺��", filesuffix
print "�ű���ǰĿ¼��", filepath#os.path.dirname(abspath)
print "�ű���ǰ����·����", abspath


for i in range(1, len(sys.argv)):

    print "����", i, sys.argv[i]
