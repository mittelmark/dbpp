"""
Demo apllication for dbpp.widgets.
"""
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.GuiBaseClass import GuiBaseClass
from dbpp.widgets.Scrolled import Scrolled
from dbpp.widgets.LabEntry import LabEntry
from dbpp.widgets.Balloon import Balloon
from dbpp.widgets.XTableView import XTableView as tv

if __name__ == '__main__':
    root=tk.Tk()
    bapp = GuiBaseClass(root) 
    # example for using the BaseClass in other applications
    bapp.addEditMenu(target=None)
    mnu=bapp.getMenu('Tools',underline=0)
    mnu.add_command(label='Test',command=lambda: print('Test'))    
    
    # example for using getFrame
    frm=bapp.getFrame()
    frm1 = ttk.Frame(frm)
    var=tk.StringVar()
    var.set("Hello")
    dgl1=LabEntry(frm1, labeltext="This",textvariable=var)
    passw=tk.StringVar()
    passw.set("secret-0815")
    dgl2=LabEntry(frm1, labeltext="Password (hover)",textvariable=passw,show="*")  
    dgl1.pack(side='top',fill="x",expand=True)
    dgl2.pack(side='top',fill="x",expand=True)  
    dgl2.label.configure(foreground="red")
    Balloon(dgl2.entry,"this is your password")
    Balloon(dgl2.label,"Hover right the password!")    
    frm2 = ttk.Frame(frm)
    txt=tk.Text(frm2,undo=True)
    Scrolled(txt)
    for i in range(0,150):
        txt.insert("end",f"line {i} the crazy blue frog jumps over the busy street ....\n")
        
    #txt.pack(side='top',fill='both',expand=True)
    bapp.setEditTarget(txt)
    tview = tv(frm)
    tview.insertData(['Col1','Col2','Col3'],
        data=[['val1.1','val1.2','val1.3'], ['val2.1','val2.2','val2.3'],
            ['val3.1','val3.2','val3.3']])

    #tview.pack(side='top',fill='both',expand=True)
    frm1.pack(side="top",fill="x")
    frm2.pack(side="top",fill="both",expand=True)
    tview.pack(side="top",fill="both",expand=True)
    bapp.addStatusBar()
    bapp.mainLoop()
