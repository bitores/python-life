# -*- coding: cp936 -*-
from threading import Thread
from Queue import Queue
from time import sleep
#q���������
#NUM�ǲ����߳�����
#JOBS���ж�������
q = Queue()
NUM = 2
JOBS = 10
#����Ĵ�������������������
def do_somthing_using(arguments):
    print arguments
#����ǹ������̣����𲻶ϴӶ���ȡ���ݲ�����
def working():
    while True:
        arguments = q.get()
        do_somthing_using(arguments)
        sleep(1)
        q.task_done()
#fork NUM���̵߳ȴ�����
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()
#��JOBS�������
for i in range(JOBS):
    q.put(i)
#�ȴ�����JOBS���
q.join()
