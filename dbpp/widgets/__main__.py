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
    
    # Notebook 1
    frm1 = ttk.Frame(nb)
    nb.add(frm1,text="LabEntry and Balloon")
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
    
    # Notebook 2
    frm2 = ttk.Frame(nb)
    nb.add(frm2,text="Scrolled Text")

    txt=tk.Text(frm2,undo=True)
    Scrolled(txt)
    for i in range(0,150):
        txt.insert("end",f"line {i} the crazy blue frog jumps over the busy street ....\n")
    #    .pack(side='top',fill='both',expand=True)
    bapp.setEditTarget(txt)
    
    # Notebook 3
    tview = tv(nb)
    nb.add(tview,text="TableView")
    tview.insertData(['Col1','Col2','Col3'],
        data=[['val1.1','val1.2','val1.3'], ['val2.1','val2.2','val2.3'],
            ['val3.1','val3.2','val3.3']])

    # Notebook 4    
    frm4 = ttk.Frame(nb)
    nb.add(frm4,text="TreeView")
    dgtree=trview(frm4,sheetsym=False)
    dgtree.configure(columns=("one","two"))
    dgtree.column("one", width=100 )
    dgtree.column("two", width=100)
    dgtree.heading("#0", text="tree column")    
    dgtree.heading("one", text="column A")
    dgtree.heading("two", text="column B")
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
    dgtree2=trview(frm4,sheetsym=True)
    dgtree2.heading("#0", text="Database Structure")    
    for tab in [1, 2, 3, 4]:
        id=dgtree2.insert("",'end',text="Table"+str(tab))
        for col in ['a','b','c']:
           dgtree2.insert(id,'end',text="Col"+str(col))
    dgtree2.bookify()        
    dgtree.pack(side="top",fill="both",expand=True)
    dgtree2.pack(side="top",fill="both",expand=True)
    
    # Notebook 5   
    frm5 = ttk.Frame(nb)
    nb.add(frm5,text="Text Mixins")
    class text(tk.Text,TextFontIncreaserMixin,TextCuaBindingsMixin,TextHighLightMixin): pass
    txt  = text(frm5,undo=True,height=50) 
    txt.bindTextResize()
    txt.bindCua()
    txt.addHighLights(commentline="'",commentstart="/'",commentend="'/",keywords=[ ['@startuml','@enduml'], ['class', 'entity', 'table'] ])
    txt.insert("1.0","@startuml\n'This is a comment\nclass A\nclass B\nA --> B\n@enduml\n")
    txt.updateHighLights()
    txt.pack(side="top",fill="both",expand=True)
    
    # Notebook 6
    frm6 = ttk.Frame(nb)
    nb.add(frm6,text="Ctext")
    ctext = Ctext(frm6) 
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
    ctext.pack(side="top",fill="both",expand=True)
    #ctext.pack(side='top',fill='x',expand=True)
    
    # Notebook 7
    frm7 = ttk.Frame(nb)
    txt2 = text(frm7)
    txt2.bindTextResize()
    txt2.bindCua()
    Scrolled(txt2)
    nb.add(frm7,text="Source")
    file = open(__file__,'r')
    for line in file:
        txt2.insert('end',line)
    txt2.addHighLights(commentline='^\s*#',commentstart='"""',commentend='"""',keywords=[ 
        ['True','False','None'],
        ['import','from','def','for', 'class', 'in', 'is', 'as', 'while','if','elif','else'] ])  
    txt2.updateHighLights()      
    nb.pack(side="top",fill="both",expand=True)
    bapp.addStatusBar()
    bapp.mainLoop()
