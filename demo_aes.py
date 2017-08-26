# -*- coding: cp936 -*-
#A Test to Return a AES-File of a Common File

from Crypto.Cipher import AES
from Crypto import Random
import binascii

def AES_File(fs):
    key = b'1234567890!@#$%^' #16-bytes password
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    print 'if fs is a multiple of 16...'
    #if fs is a multiple of 16
    x = len(fs) % 16
    print 'fs的长度是： ', len(fs)
    print 'The num to padded is : ', x
    if x != 0:
        fs_pad = fs + '0'*(16 - x) #It shoud be 16-x not 
        print 'fs_pad is : ', fs_pad
        print len(fs_pad)
        print len(fs_pad)%16
    msg = iv + cipher.encrypt(fs_pad)
    print 'File after AES is like...', binascii.b2a_hex(msg[:10])
    return msg

#Create a Test Src File and Get FileSteam
fs = open('test', 'w+')
fs.write('啊，我爱你，我的祖国！')
fs.write('凌晨三时开始进攻！')
fs.seek(0,0)
fs_msg = fs.read()
print fs_msg
fs.close()

#Crypt Src FileStream
fc = open('fc', 'wb')
fc_msg = AES_File(fs_msg)
fc.writelines(fc_msg)
fc.close()

raw_input('Enter for Exit...')
