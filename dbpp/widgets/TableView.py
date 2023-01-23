#!/usr/bin/python3
"""
Table widget based on ttk.Treeview with scrollbars shown if needed.
  
This a widget to display tabular data using the standard ttk.Treeview widget, 
inheriting all its methods and options.
Further the widget has automatically shown or hidden scrollbars. 
A convenience function to load tabular data is implemented as well.

Examples:

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.TableView import TableView 
root = tk.Tk()
root.title('TableView demo')
dgtab=TableView(root)
dgtab.pack(side='top',fill='both',expand=True)
dgtab.readTabfile("iris.tab")
```
  
**Author:** Detlef Groth, University of Potsdam, 2019-2023

**License:** MIT - License

"""
import tkinter as tk 
import tkinter.ttk as ttk

#import sqlite3
class TableView (ttk.Treeview):
    #'
    #' ## Commands
    #'  
    #'  **TableView(parent,...)**
    #'  
    def __init__(self,parent,*args, **kwargs):
        """The constructor to create a TableView widget.

        Args:
            parent (ttk.Frame):the parent widget wherein the ttk.Treeview widget will be placed.
            *args (list): standard ttk.Treeview arguments which will be delegated to the widget
            **kwargs (dict): standard ttk.Treeview arguments which will be delegated to the widget
        
        Returns:
            TableView widget with addtional methods and all methods of a ttk.Treeview widget
        """    
        self.frame=ttk.Frame(parent)
        ttk.Treeview.__init__(self, self.frame,*args,**kwargs)
        self.tag_configure('even', background='#CCEEFF')
        self.tag_configure('odd', background='#FFFFFF')        
        self.column("#0",width=0,minwidth=0,stretch=False)

    def getFrame(self):
        """Returns the frame in which the widget is embedded to perform, useful for packing or gridding the widget.
        
        This function is needed by geometry managers like grid or ttk.PanedWindow to manage the parent frame of
        the widget in the layout. For pack the default methods pack and pack_forget are defined.
        """
        # geometry manager needs the frame
        return(self.frame)

    def readTabfile(self,filename):
        """Reads a tabular formatted data file and displays it into the `TableView` widget.
    
        Args:
            filename (string): the name of a tabular file
        """
        self.delete(*self.get_children())
        i = 0
        file = open(filename,"r")
        for line in file:
            cells= line.split("\t")
            if i == 0:
                for j in range(1,len(cells)+1):
                    if j == 1:
                        l=["col"+str(j)]
                    else:
                        l.append("col"+str(j))
                self.configure(columns=l)
                for j in range(1,len(cells)+1):
                    col="col"+str(j)
                    self.heading(col,text=cells[j-1])
                i = i + 1
            else:
                if i % 2 == 0:
                    tag="even"
                else:
                    tag ="odd"
                self.insert("",'end',values=cells,tag=tag)
                i=i+1
                
    def pack(self,**kwargs):
        """Overwrites the default pack method to use the internal frame."""
        self.frame.pack(kwargs) 
    def pack_forget(self,**kwargs):
        """Overwrites the default pack_forget method to use the internal frame."""
        self.frame.pack_forget(kwargs) 
        
if __name__ == '__main__':
    from os.path import dirname, realpath, sep, pardir, join
    import sys
    iris_path=join(dirname(realpath(__file__)),"..","..","data") + sep + "iris.tab"
    root = tk.Tk()
    root.title('DGApp')
    pw=ttk.PanedWindow(root,width=400,height=400)
    dgtab=TableView(pw)
    #dgtab.pack(side='top',fill='both',expand=True)
    pw.add(dgtab.getFrame())
    pw.pack(side='top',fill='both',expand=True)
    dgtab.readTabfile(iris_path)
    #dgtab.readTabfile("../../data/ss_aa_matrix.txt")
    dgtab2=TableView(pw)
    pw.add(dgtab2.getFrame())
    #dgtab2.pack(side='top',fill='both',expand=True)
    dgtab2.configure(columns=('A','B','C'))
    dgtab2.heading('A',text="A Column")
    dgtab2.heading('B',text="B Column")
    dgtab2.heading('C',text="C Column")
    for i in range(0,5):
        dgtab2.insert("","end",values=('A1','A2','A3'))
    #dgtab2.pack_forget()
    root.geometry("400x300")
    root.mainloop()

