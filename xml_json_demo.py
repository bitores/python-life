#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【折腾】Python中xml和Json之间相互转换：xml转json，json转xml
http://www.crifan.com/python_convertion_between_xml_and_json
 
Version:    2013-05-15
Author:     Crifan
Contact:    admin (at) crifan.com
"""
 
import xmltodict;
import json;
 
def pythonXmlToJson():
    """
        demo Python xml to json
    """
    xmlStr = """
<student>
    <stid>10213</stid>
    <info>
        <name>name</name>
        <mail>xxx@xxx.com</mail>
        <sex>male</sex>
    </info>
    <course>
        <name>math</name>
        <score>90</score>
    </course>
    <course>
        <name>english</name>
        <score>88</score>
    </course>
</student>
"""
 
    convertedDict = xmltodict.parse(xmlStr);
    jsonStr = json.dumps(convertedDict);
    print "jsonStr=",jsonStr;
    jsonStr = json.dumps(convertedDict, indent=1);
    print "jsonStr=",jsonStr;
 
###############################################################################
if __name__=="__main__":
    pythonXmlToJson();
