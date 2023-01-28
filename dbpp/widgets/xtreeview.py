#!/usr/bin/python3
"""
Tree widget based on ttk.Treeview with scrollbars shown if needed and default images.

This a widget to tree like data using the standard ttk.Treeview widget, 
inheriting all its methods and options.
Further the widget has automatically shown or hidden scrollbars and as 
well some default images which simplify creating nice tree widgets.
To use the pack geometry manager you can just use the pack and the 
pack_forget commands of this widget as these are forwarded to the frame. 
For other geometry managers like grid, the panedwindow or the notenbook you should use the [getFrame](#getFrame) method.

Examples:

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpb.widgets.XTreeView import XTreeView
root = tk.Tk()
root.title('DGApp')
dgtree=XTreeView(root,sheetsym=False)
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

dgtree.insert("", 3, "dir3", text="Dir 3")
dgtree.insert("dir3", 3,
   text=" sub dir 3",values=("3A"," 3B"))
def printSelection(event):
   item = dgtree.identify('item',event.x,event.y)
   print(item)
dgtree.bind("<Double-1>",printSelection)
dgtree.bookify()
root.mainloop()
```


![](XTreeView.png)

**Author:** Detlef Groth, University of Potsdam, 2019-2023

**License:** MIT - License

"""

import tkinter.ttk as ttk
import tkinter as tk 
from dbpp.widgets.scrolled import Scrolled
 
class XTreeView (ttk.Treeview):
    """Extended ttk.Treeview widget."""
    def __init__(self,parent,sheetsym=False,*args, **kwargs):
        """The constructor to create a XTreeView widget.
          
        Args:
            parent (ttk.Frame): the parent widget wherein the ttk.Treeview widget will be placed.
            sheetsym (bool): should table sheet symbols be shown, defaults to False
            *args (list): standard ttk.Treeview arguments which will be delegated to the widget
            **kwargs (dict): standard ttk.Treeview arguments which will be delegated to the widget
        """
        self.frame=ttk.Frame(parent)
        ttk.Treeview.__init__(self, self.frame)
        Scrolled(self)        
        self.sheetsym=sheetsym
        # expose some text methods as methods on this object
        # inefficient must write all methods here
        # better us get attribute
        # self.get_children = self.get_children
        
        #  some photos
        self.photoContents=tk.PhotoImage(data="""
        R0lGODlhEAAQAIQAAPwCBJyenJyanKSepHRudPT29PTy9Ly6vLS2tGxubPz+
        /Pz6/Ly2vPz2/LSytFxaXOTi5IyKjPTu9Ozm7NTW1OTm5MTCxOTe5Nze3NzW
        3NTS1MzGzMzOzKymrMS+xKyqrCH5BAEAAAAALAAAAAAQABAAAAWDIAAEwiCQ
        JiGuolAY73sgCdsWypIrDF+zgoZOpzgoFI4HEDdUCAgJgnIVXFh1DQgjMr0J
        r5IJ5dAFVBeNRiFcsZRd17WkcnED0wtJYTLBYMhLaQ0SEhcXGQxvaoOFFxQa
        SUsLBnOHGRuRVAWMhxQcGx1vfZ8bHg4OHx9lUg+trq8ifiEAIf5oQ3JlYXRl
        ZCBieSBCTVBUb0dJRiBQcm8gdmVyc2lvbiAyLjUNCqkgRGV2ZWxDb3IgMTk5
        NywxOTk4LiBBbGwgcmlnaHRzIHJlc2VydmVkLg0KaHR0cDovL3d3dy5kZXZl
        bGNvci5jb20AOw==""")

        self.photoBookClosed=tk.PhotoImage(data="""
        R0lGODlhEAAQAIUAAPwCBAROdARahBRejBx6rBxypFSexDySxDSGvAxulDR2
        nHSy1IS23FyixDySvBRupAxilMze7Iy+1IS21KTK3ESWxARijIy+3FyizCR+
        tAxmjARWhMze9AQ+XAxejARSfAQyRERyhPz6/PTu9Nzq9KzS5FyClPz+/PTy
        9KSmpDRmfLS2tCRSZOTm7Ly2vCxadAQ+VAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAQABAAAAaD
        QIBwSCwahQHBsRgYEAqBJaBpOCAIiShTsWAsGg7CA6JFRiQTCsNQEVsE5UAg
        cvFiHJmHZiNHagIcEw0VGVgCfH0dAWQcF1cFCR4fASBDimRnDwlkISIjRIpZ
        JCUfJiInKCkdoIsBKiciKCssq0WKHS0oLi8wUh0dKSG1UgAww8TIfkEAIf5o
        Q3JlYXRlZCBieSBCTVBUb0dJRiBQcm8gdmVyc2lvbiAyLjUNCqkgRGV2ZWxD
        b3IgMTk5NywxOTk4LiBBbGwgcmlnaHRzIHJlc2VydmVkLg0KaHR0cDovL3d3
        dy5kZXZlbGNvci5jb20AOw==""")
        self.photoBookOpend=tk.PhotoImage(data="""
        R0lGODlhEAAQAIUAAPwCBAQCBExCNGSenHRmVCwqJPTq1GxeTHRqXPz+/Dwy
        JPTq3Ny+lOzexPzy5HRuVFSWlNzClPTexIR2ZOzevPz29AxqbPz6/IR+ZDyK
        jPTy5IyCZPz27ESOjJySfDSGhPTm1PTizJSKdDSChNzWxMS2nIR6ZKyijNzO
        rOzWtIx+bLSifNTGrMy6lIx+ZCRWRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAQABAAAAae
        QEAAQCwWBYJiYEAoGAFIw0E5QCScAIVikUgQqNargtFwdB9KSDhxiEjMiUlg
        HlB3E48IpdKdLCxzEAQJFxUTblwJGH9zGQgVGhUbbhxdG4wBHQQaCwaTb10e
        mB8EBiAhInp8CSKYIw8kDRSfDiUmJ4xCIxMoKSoRJRMrJyy5uhMtLisTLCQk
        C8bHGBMj1daARgEjLyN03kPZc09FfkEAIf5oQ3JlYXRlZCBieSBCTVBUb0dJ
        RiBQcm8gdmVyc2lvbiAyLjUNCqkgRGV2ZWxDb3IgMTk5NywxOTk4LiBBbGwg
        cmlnaHRzIHJlc2VydmVkLg0KaHR0cDovL3d3dy5kZXZlbGNvci5jb20AOw==""")
        self.photoSheet=tk.PhotoImage(data="""
        R0lGODlhEAAQAIIAAPwCBAQCBAT+/Pz+/KSipPz+BAAAAAAAACH5BAEAAAAA
        LAAAAAAQABAAAANFCBDc7iqIKUW98WkWpx1DAIphR41ouWya+YVpoBAaCKtM
        oRfsyue8WGC3YxBii5+RtiEWmASFdDVs6GRTKfCa7UK6AH8CACH+aENyZWF0
        ZWQgYnkgQk1QVG9HSUYgUHJvIHZlcnNpb24gMi41DQqpIERldmVsQ29yIDE5
        OTcsMTk5OC4gQWxsIHJpZ2h0cyByZXNlcnZlZC4NCmh0dHA6Ly93d3cuZGV2
        ZWxjb3IuY29tADs=""")
        self.photoFile=tk.PhotoImage(data="""
        R0lGODlhEAAQAIUAAPwCBFxaXNze3Ly2rJSWjPz+/Ozq7GxqbJyanPT29HRy
        dMzOzDQyNIyKjERCROTi3Pz69PTy7Pzy7PTu5Ozm3LyqlJyWlJSSjJSOhOzi
        1LyulPz27PTq3PTm1OzezLyqjIyKhJSKfOzaxPz29OzizLyidIyGdIyCdOTO
        pLymhOzavOTStMTCtMS+rMS6pMSynMSulLyedAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAQABAAAAaQ
        QIAQECgajcNkQMBkDgKEQFK4LFgLhkMBIVUKroWEYlEgMLxbBKLQUBwc52Hg
        AQ4LBo049atWQyIPA3pEdFcQEhMUFYNVagQWFxgZGoxfYRsTHB0eH5UJCJAY
        ICEinUoPIxIcHCQkIiIllQYEGCEhJicoKYwPmiQeKisrKLFKLCwtLi8wHyUl
        MYwM0tPUDH5BACH+aENyZWF0ZWQgYnkgQk1QVG9HSUYgUHJvIHZlcnNpb24g
        Mi41DQqpIERldmVsQ29yIDE5OTcsMTk5OC4gQWxsIHJpZ2h0cyByZXNlcnZl
        ZC4NCmh0dHA6Ly93d3cuZGV2ZWxjb3IuY29tADs=""")
        self.bind("<<TreeviewOpen>>",self._openFolder)                    
        self.bind("<<TreeviewClose>>",self._closeFolder)
        #self.bind("<Double-1>", self._OnDoubleClick)                    

    def bookify (self,item=''):
      """Displays all images in the tree widget, starting from root or from the given item.
   
      Args: 
          item (ttk.Treeview item): the parent item from where the images, should be initialized, defaults to the empty string, the root item.
      """
      if not(self.sheetsym):
        for child in self.get_children(item):
            if len(self.get_children(child))>0:
                self.item(child,image=self.photoBookClosed)
                self.bookify(child)
            else:
                self.item(child,image=self.photoContents)
      else:
        for child in self.get_children(item):
            if len(self.get_children(child))>0:
                self.item(child,image=self.photoSheet)
                self.bookify(child)
            else:
                self.item(child,image=self.photoFile)
    def getFrame(self):
        """Returns the frame in which the widget is embedded to perform, useful for packing or gridding the widget.
        
        This function is needed by geometry managers like grid or ttk.PanedWindow to manage the parent frame of
        the widget in the layout. For pack the default methods pack and pack_forget are defined."""
        # geometry manager needs the frame
        return(self.frame)

          
    def _openFolder(self, event):
      if not(self.sheetsym):
         item=self.selection()[0]
         if len(self.get_children(item))>0:
             self.item(item,image=self.photoBookOpend)
    def _closeFolder(self, event):
      if not(self.sheetsym):
         item=self.selection()[0]

         #         item=self.tree.identify('item',event.x,event.y)
         if len(self.get_children(item))>0:
             self.item(item,image=self.photoBookClosed)
    def pack(self,**kwargs):
        """Overwrites the default pack method to use the internal frame."""
        self.frame.pack(kwargs)    
    def pack_forget(self,**kwargs):
        """Overwrites the default pack_forget method to use the internal frame."""
        self.frame.pack_forget(kwargs)    
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title('DGApp')
    dgtree=XTreeView(root,sheetsym=False)
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
    dgtree2=XTreeView(root,sheetsym=True)
    dgtree2.heading("#0", text="Database Structure")    
    for tab in [1, 2, 3, 4]:
        id=dgtree2.insert("",'end',text="Table"+str(tab))
        for col in ['a','b','c']:
           dgtree2.insert(id,'end',text="Col"+str(col))
    dgtree2.bookify()        
    dgtree.pack(side='top',fill='both',expand=True)   
    dgtree2.pack(side='top',fill='both',expand=True)       
    root.mainloop()

