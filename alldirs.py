# -*- coding: cp936 -*-
import os
import os.path
rootdir = "d:\phpweb\god"                                   # ָ�����������ļ���

for root,dirs,files in os.walk(rootdir):   #�����������ֱ𷵻�1.��Ŀ¼ 2.�����ļ������֣�����·���� 3.�����ļ�����
    for dirname in dirs:                       #����ļ�����Ϣ
        print "parent is:" + root
        print  "dirname is" + dirname

    for filename in files:                        #����ļ���Ϣ
        print "parent is:" + root
        print "filename is:" + filename
        print "the full name of the file is:" + os.path.join(root,filename) #����ļ�·����Ϣ
