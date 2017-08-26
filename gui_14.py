import sys
import os
import Tkinter
from tkdnd_wrapper import TkDND
import shlex, subprocess
from subprocess import Popen, PIPE
import glob
import shutil

root = Tkinter.Tk()
dnd = TkDND(root)
entry = Tkinter.Entry()
entry.grid()

def handle(event):
    inputfilespath = event.data
    event.widget.insert(0, inputfilespath)
    filesdir = os.path.dirname(os.path.realpath(inputfilespath))
    files = glob.iglob(os.path.join(filesdir, "*.myext"))
    for inputfilespath in files:
        if os.path.isfile(inputfilespath):
            subprocess1 = subprocess.Popen([...conversion command given as list, not string...], shell=True)
            print "\n\nConversione in corso..."
            subprocess1.wait()
            subprocess1.terminate()
            print "\n\nProcesso terminato!"

dnd.bindtarget(entry, handle, 'text/uri-list')
root.mainloop()
