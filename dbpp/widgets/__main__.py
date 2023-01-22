"""
Demo apllication for dbpp.widgets.
"""
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.GuiBaseClass import GuiBaseClass
from dbpp.widgets.Scrolled import Scrolled
if __name__ == '__main__':
    root=tk.Tk()
    bapp = GuiBaseClass(root) 
    # example for using the BaseClass in other applications
    bapp.addEditMenu(target=None)
    mnu=bapp.getMenu('Tools',underline=0)
    mnu.add_command(label='Test',command=lambda: print('Test'))    
    
    # example for using getFrame
    frm=bapp.getFrame()
    txt=tk.Text(frm,undo=True)
    Scrolled(txt)
    for i in range(0,150):
        txt.insert("end",f"line {i} the crazy blue frog jumps over the busy street ....\n")
        
    #txt.pack(side='top',fill='both',expand=True)
    bapp.setEditTarget(txt)
    bapp.addStatusBar()
    bapp.mainLoop()
