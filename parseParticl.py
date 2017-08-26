import re
import string


file_object = open("test.particle","r")
lines = file_object.readlines()
for line in lines:
   #print line
    L = string.split(line)
    if len(L)==0:
        continue
    elif len(L) == 1:
        if L[0]=='{':
            print L[0]
        elif L[0]=='}':
            print L[0]
    elif len(L) == 2:
        print L[0],' ',L[1]
    elif len(L) == 3:
        print L[0],' ',L[1],' ',L[2]
    elif len(L) == 4:
        tp = tuple(L)
        tp = tp[-3:]
        tp = ' '.join(map(str,tp))
        print L[0],',',tp
        
    


    
print "\nsuccess"
file_object.close()
