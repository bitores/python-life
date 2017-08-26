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
 
        #以下代码参考：
        #http://bytes.com/topic/python/answers/855640-hooking-windowsmessages-python
 
        self.hwnd = eval(self.master.wm_frame())
        #toplevel.wm_frame():Return identifier for decorative frame of this widget if present.
 
        print 'hwnd:%s, title:%s' % (self.hwnd, win32gui.GetWindowText(self.hwnd))
        #title为空
 
        #设置窗口允许接收拖放的文件
        win32gui.DragAcceptFiles(self.hwnd, 1)
 
        self.wnd = win32ui.CreateWindowFromHandle(self.hwnd)
        #win32ui模块的方法，而非win32gui
        self.wnd.HookMessage(self.OnDropFiles, win32con.WM_DROPFILES)
        #上面这句和下面这句有什么区别？
        #self.master.protocol('WM_DROPFILES', self.OnDropFiles)
        #为什么捕获不到WM_DROPFILES消息？
 
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
        #响应拖放消息的方法
        #这个方法从来没有被执行
        print 'Drag and drop'
 
        filenamebuffering=''
        #获取拖放的文件总数
        #hDropInfo=msg[2]
        hDropInfo=win32con.WM_DROPFILES
        #filescount = win32gui.DragQueryFile(win32con.WM_DROPFILES, 0xFFFFFFFF, None, 0)
        filescount = win32api.DragQueryFile(win32con.WM_DROPFILES, 0xFFFFFFFF, None, 0)
        #filescount = win32api.DragQueryFile(hDropInfo)
 
        for i in range(filescount):
            #获取文件名
            #filename=win32gui.DragQueryFile(hDropInfo, i, filenamebuffering, 100)
            filename=win32api.DragQueryFile(hDropInfo, i, filenamebuffering, 100)
            #filename=win32api.DragQueryFile(hDropInfo, i)
            #保存文件名
            self.files.append(filename)
        #清除缓存
        win32gui.DragFinish(hDropInfo)
        return 0
 
 
if __name__=='__main__':
    root=Tk()
    app=App(root)
    #Entry(root).pack()
    app.mainloop()
         
'''关于HookMessage还有一个相关的网页，里面的代码如下
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
        #如果使用其他GUI框架，比如Tkinter，HookMessage()方法怎么用？
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
