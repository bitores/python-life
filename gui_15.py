import Tkinter as tk

class PasswordDialog(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self)
        self.password = None
        self.entry = tk.Entry(self, show='*')
        self.entry.pack()
        self.button = tk.Button(self)
        self.button["text"] = "Submit"
        self.button["command"] = self.StorePass
        self.button.pack()

    def StorePass(self):
        self.password = self.entry.get()
        self.destroy()
        print '1: Password was', self.password

class MainApplication(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.button = tk.Button(self)
        self.button["text"] = "Password"
        self.button["command"] = self.GetPassword
        self.button.pack()

    def GetPassword(self):
        passwd = PasswordDialog(self)
        # HALT HERE 
        print '2: Password was', passwd.password

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
