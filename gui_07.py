# -*- coding: cp936 -*-
import Tkinter
root=Tkinter.Tk()
label=Tkinter.Label(root,text='hello ,python')
label.pack()      #��LABEL�����ӵ��׿���
button1=Tkinter.Button(root,text='BUTTON1')
button1.pack(side=Tkinter.LEFT)
button2=Tkinter.Button(root,text='BUTTON2')
button2.pack(side=Tkinter.RIGHT)
root.mainloop()
