#coding:gbk
from Tkinter import *
import win32gui
import win32ui
import win32api
import win32con
 
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.master.title('note')
        self.top=self.winfo_toplevel()
        self.master=master
        self.files=[]
        self.mkwidgets()
        self.master.protocol('WM_DROPFILES', self.OnDropFiles)
        self.master.geometry('%dx%d+%d+%d' % (400,200,50,50))
 
        #���´���ο���
        #http://bytes.com/topic/python/answers/855640-hooking-windowsmessages-python
 
        self.hwnd = eval(self.master.wm_frame())
        #toplevel.wm_frame():Return identifier for decorative frame of this widget if present.
 
        print 'hwnd:%s, title:%s' % (self.hwnd, win32gui.GetWindowText(self.hwnd))
        #titleΪ��
 
        #���ô�����������Ϸŵ��ļ�
        win32gui.DragAcceptFiles(self.hwnd, 1)
 
        self.wnd = win32ui.CreateWindowFromHandle(self.hwnd)
        #win32uiģ��ķ���������win32gui
        self.wnd.HookMessage(self.OnDropFiles, win32con.WM_DROPFILES)
        #�����������������ʲô����
        #self.master.protocol('WM_DROPFILES', self.OnDropFiles)
        #Ϊʲô���񲻵�WM_DROPFILES��Ϣ��
 
    def mkwidgets(self):
        self.e=Entry(self.top)
        self.e.pack()
        self.b=Button(self.top, text='hi', command=self.click)
        self.b.pack()
        #self.after_idle(self.bindx)
 
    def click(self):
        print self.files
        self.hwnd = eval(self.master.wm_frame())
        print 'hwnd:%s, title:%s' % (self.hwnd, win32gui.GetWindowText(self.hwnd))
 
    def OnDropFiles(self,msg=None):
        #��Ӧ�Ϸ���Ϣ�ķ���
        #�����������û�б�ִ��
        print 'Drag and drop'
 
        filenamebuffering=''
        #��ȡ�Ϸŵ��ļ�����
        #hDropInfo=msg[2]
        hDropInfo=win32con.WM_DROPFILES
        #filescount = win32gui.DragQueryFile(win32con.WM_DROPFILES, 0xFFFFFFFF, None, 0)
        filescount = win32api.DragQueryFile(win32con.WM_DROPFILES, 0xFFFFFFFF, None, 0)
        #filescount = win32api.DragQueryFile(hDropInfo)
 
        for i in range(filescount):
            #��ȡ�ļ���
            #filename=win32gui.DragQueryFile(hDropInfo, i, filenamebuffering, 100)
            filename=win32api.DragQueryFile(hDropInfo, i, filenamebuffering, 100)
            #filename=win32api.DragQueryFile(hDropInfo, i)
            #�����ļ���
            self.files.append(filename)
        #�������
        win32gui.DragFinish(hDropInfo)
        return 0
 
 
if __name__=='__main__':
    root=Tk()
    app=App(root)
    #Entry(root).pack()
    app.mainloop()
         
'''����HookMessage����һ����ص���ҳ������Ĵ�������
http://www.gossamer-threads.com/lists/python/python/5723
 
from pywin.framework import dlgappcore, app 
import win32ui, win32con, win32api 
import sys 
import regsub 
 
class DropScriptDialogApp(dlgappcore.DialogApp): 
    def CreateDialog(self): 
        return DropScriptAppDialog() 
 
class DropScriptAppDialog(dlgappcore.AppDialog):
    def __init__(self): 
        self.edit = None 
        dlgappcore.AppDialog.__init__(self, win32ui.IDD_LARGE_EDIT) 
 
    def OnInitDialog(self): 
        self.SetWindowText('Drop script application') 
        self.edit = self.GetDlgItem(win32ui.IDC_EDIT1) 
        self.DragAcceptFiles()
        #���ʹ������GUI��ܣ�����Tkinter��HookMessage()������ô�ã�
        self.HookMessage(self.OnDropFiles, win32con.WM_DROPFILES)
        return 1 
 
    def OnDropFiles(self, msg): 
        hDropInfo = msg[2] 
        nFiles = win32api.DragQueryFile(hDropInfo) 
        try: 
            for iFile in range(0, nFiles): 
                fileName = win32api.DragQueryFile(hDropInfo, iFile) 
                print '%s dropped...' % fileName 
        finally: 
            win32api.DragFinish(hDropInfo)
        return 0 
 
    def PreDoModal(self): 
        sys.stdout = sys.stderr = self 
 
    def write(self, str): 
        if self.edit: 
            self.edit.SetSel(-2) 
            # translate \n to \n\r 
            self.edit.ReplaceSel(regsub.gsub('\n','\r\n',str)) 
        else: 
            win32ui.OutputDebug( 
                'dlgapp - no edit control! >>\n%s\n<<\n' % str ) 
 
app.AppBuilder = DropScriptDialogApp 
 
if __name__=='__main__': 
    import demoutils
    demoutils.NeedApp()
'''
