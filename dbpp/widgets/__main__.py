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
from dbpp.widgets.XTreeView import XTreeView as trview
from dbpp.widgets.TextMixins import *
from dbpp.widgets.Ctext import *

if __name__ == '__main__':
    root=tk.Tk()
    bapp = GuiBaseClass(root) 
    # example for using the BaseClass in other applications
    bapp.addEditMenu(target=None)
    mnu=bapp.getMenu('Tools',underline=0)
    mnu.add_command(label='Test',command=lambda: print('Test'))    
    
    # example for using getFrame
    mfrm=bapp.getFrame()
    nb = ttk.Notebook(mfrm)
    frm1 = ttk.Frame(nb)
    nb.add(frm1,text="Notebook 1")
    # top frame
    frm1a = ttk.Frame(frm1)
    var=tk.StringVar()
    var.set("Hello")
    dgl1=LabEntry(frm1a, labeltext="This",textvariable=var)
    passw=tk.StringVar()
    passw.set("secret-0815")
    dgl2=LabEntry(frm1a, labeltext="Password (hover)",textvariable=passw,show="*")  
    dgl1.pack(side='top',fill="x",expand=True)
    dgl2.pack(side='top',fill="x",expand=True)  
    dgl2.label.configure(foreground="red")
    Balloon(dgl2.entry,"this is your password")
    Balloon(dgl2.label,"Hover right the password!")    
    frm1a.pack(side="top",fill="x")
    pw=ttk.PanedWindow(frm1,orient="horizontal")
    frm1b = ttk.Frame(pw)
    txt=tk.Text(frm1b,undo=True)
    Scrolled(txt)
    for i in range(0,150):
        txt.insert("end",f"line {i} the crazy blue frog jumps over the busy street ....\n")
    #    .pack(side='top',fill='both',expand=True)
    bapp.setEditTarget(txt)
    pw.add(frm1b)
    tview = tv(pw)
    tview.insertData(['Col1','Col2','Col3'],
        data=[['val1.1','val1.2','val1.3'], ['val2.1','val2.2','val2.3'],
            ['val3.1','val3.2','val3.3']])
    pw.add(tview.getFrame())
    tview.pack(side="top",expand=True,fill="both")
    pw.pack(side="top",expand=True,fill="both")
    frmr = ttk.PanedWindow(nb)
    nb.add(frmr,text="Notebook 2")
    dgtree=trview(frmr,sheetsym=False)
    dgtree.configure(columns=("one","two"))
    dgtree.column("one", width=100 )
    dgtree.column("two", width=100)
    dgtree.heading("#0", text="tree column")    
    dgtree.heading("one", text="column A")
    dgtree.heading("two", text="column B")
    #
    dgtree.insert("",0,text="Line 1",values=("1A","1b")),
    id2 = dgtree.insert("",1,"dir2",text="Dir 2")
    dgtree.insert(id2,"end","dir 2",
        text="sub dir 2", values=("2A","2B"))
    ###alternatively:
    dgtree.insert("", 3, "dir3", text="Dir 3")
    dgtree.insert("dir3", 3,
        text=" sub dir 3",values=("3A"," 3B"))
    #dgtree.pack()
    def printSelection(event):
        item = dgtree.identify('item',event.x,event.y)
        print(item)
        #print(dgtree.item(item,text=Null))

    dgtree.bind("<Double-1>",printSelection)
    dgtree.bookify()
    dgtree2=trview(frmr,sheetsym=True)
    dgtree2.heading("#0", text="Database Structure")    
    for tab in [1, 2, 3, 4]:
        id=dgtree2.insert("",'end',text="Table"+str(tab))
        for col in ['a','b','c']:
           dgtree2.insert(id,'end',text="Col"+str(col))
    dgtree2.bookify()        
    frmr.add(dgtree.getFrame())
    frmr.add(dgtree2.getFrame())
    frm3 = ttk.Frame(nb)
    nb.add(frm3,text="Notebook 3")
    class text(tk.Text,TextFontIncreaserMixin,TextCuaBindingsMixin,TextHighLightMixin): pass
    txt  = text(frm3,undo=True,height=50) 
    txt.bindTextResize()
    txt.bindCua()
    txt.addHighLights(commentline="'",commentstart="/'",commentend="'/",keywords=[ ['@startuml','@enduml'], ['class', 'entity', 'table'] ])
    txt.insert("1.0","@startuml\n'This is a comment\nclass A\nclass B\nA --> B\n@enduml\n")
    txt.updateHighLights()
    frm4 = ttk.Frame(nb)
    nb.add(frm3,text="Notebook 4")

    ctext = Ctext(frm4) 
    ctext.add_highlight_class('DML1', 'blue', ['select','SELECT','from','FROM'])
    ctext.add_highlight_class('DML2', 'blue', ['and', 'AND', 'as','AS', 'asc', 'ASC', 
    		'between','BETWEEN', 'by', 'BY', 'desc','DESC', 'distinct', 'DISTINCT', 'group','GROUP', 		'having', 'HAVING','in','IN','inner', 'INNER', 'join', 'JOIN', 'left', 'LEFT', 'like','LIKE', 		'limit','LIMIT', 'max','MAX','min','MIN', 'or', 'OR', 'order',  'ORDER', 'outer', 'OUTER', 		'right', 'RIGHT', 'round', 'ROUND','where','WHERE', ])
    ctext.add_highlight_class('functions','OrangeRed3', ['avg', 'AVG', 'count','COUNT', 		
        'except','EXCEPT', 'intersect','INTERSECT', 'sum', 'SUM', 'union','UNION'])
    ctext.add_highlight_chars('math operators', 'magenta', ['*','>','<','='])    	
    ctext.add_highlight_regexp("comment","dark green", "--.+")
    ctext.add_highlight_regexp("string","magenta", "['\"].+?['\"]")
    ctext.enable_c_comments(True)

    ctext.tag_configure('_cComment',foreground="dark green")
    ctext.insert("end", "select * from sample where id == '1' or id == \"Hello\"\n-- a comment\n new statement\n/*\nc-style comment passing\n multiple lines\n*/")
    ctext.highlight('1.0','end')
    #ctext.pack(side='top',fill='x',expand=True)
    nb.pack(side="top",fill="both",expand=True)
    bapp.addStatusBar()
    bapp.mainLoop()
