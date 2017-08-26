#!/usr/bin/env python
#coding=gb2312
import os 
import time 
 
PATH = lambda p: os.path.abspath(p) 
 
def screenshot(): 
    path = PATH(os.getcwd() + "/screenshot") 
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) 
    os.popen("adb wait-for-device") 
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/screenshot")): 
        os.makedirs(path) 
    os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png")) 
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    print "success"
 
if __name__ == "__main__": 
    screenshot()
    raw_input()
