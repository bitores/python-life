# -*- coding: cp936 -*-
import xml.parsers.expat
#���ƴ�ӡ����
level = 0
#��ȡĳ�ڵ����Ƽ�����ֵ����
def start_element(name,attrs):
    global level
    print ' '*level,'Start element:',name,attrs
    level = level + 1
#��ȡĳ�ڵ��������
def end_element(name):
    global level
    level = level + 1
    print ' '*level,'End element:',name
#��ȡĳ�ڵ��м��ֵ
def char_data(data):
    if(data == '\n'):
        return
    if(data.isspace()):
        return
    global level
    print ' '*level,'Character data:',data

p = xml.parsers.expat.ParserCreate()
f = file('sample.xml')
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data
p.returns_unicode = False
p.ParseFile(f)
f.close()
    
