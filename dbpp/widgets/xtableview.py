#!/usr/bin/python3
"""
Extension of the TableView widget which can as well insert lists into the ttk.Treeview widget.

The widget TableView provides an extension for the [TableView](tableview.md) 
table widget with a readData function, getting header and lists 
inheriting all methods and options from `TableView`.

Hint: This functionality should be better implemented as a Mixin.

Below you see the inheritance hierarchy and the added methods:

```{.kroki echo=false dia=plantuml}
@startuml
class "ttk.TreeView" as Treeview {
    configure(kwargs)
    cget("property")
    etc()
}
class "dbpp.widgets.TableView" as TableView {
    readTabfile(filename)
    pack(kwargs)
    pack_forget()
}
class "dbpp.widgets.XTableView" as XTableView {
    insert_data(colnames,data)
}
Treeview <- TableView
TableView <- XTableView
@enduml
```

Examples:
 
```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.XTableView import XTableView 
root = tk.Tk()
root.title('XTableView Demo')
dgtab=XTableView(root)
dgtab.getFrame().pack(side='top',fill='both',expand=True)
dgtab.insert_data(['Col1','Col2'],
    data=[['val1.1','val1.2'], ['val2.1','val2.2']])
root.geometry("400x300")
root.mainloop()
```

![](XTableView.png)

**Author:** Detlef Groth, University of Potsdam, 2019-2023

**License:** MIT - License

"""
import tkinter.ttk as ttk
import tkinter as tk 
import dbpp.widgets.tableview as tv


#import sqlite3
class XTableView (tv.TableView):
    """Extended ttk.Treeview based on TableView."""
    
    def __init__(self,parent,*args, **kwargs):
        """The constructor to create a XTableView widget.

        Args:
            parent (ttk.Frame):the parent widget wherein the ttk.Treeview widget will be placed.
            *args (list): standard ttk.Treeview arguments which will be delegated to the widget
            **kwargs (dict): standard ttk.Treeview arguments which will be delegated to the widget
        
        Returns:
            XTableView widget with addtional methods and all methods of a ttk.Treeview widget
        """    

        tv.TableView.__init__(self, parent,*args,**kwargs)

    def insert_data(self, colnames="", data=""):
        """Inserts data into a ttk.Treeview widget.
        
        Args:
            colnames (list): list of column nanes
            data (list): nested list of data
        """
        i=0
        self.delete(*self.get_children())
        self.configure(columns=tuple(colnames))
        for item in colnames:
            self.heading(item, text=str(item))
        for row in data:
            if i % 2 == 0:
                tag="even"
            else:
                tag ="odd"
            self.insert('',tk.END, values=row,tag=tag)
            i=i+1
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title('XTableView Demo')
    dgtab=XTableView(root)
    dgtab.pack(side='top',fill='both',expand=True)
    dgtab.insert_data(['Col1','Col2'],
        data=[['val1.1','val1.2'], ['val2.1','val2.2']])
            
    root.geometry("400x300")
    root.mainloop()

