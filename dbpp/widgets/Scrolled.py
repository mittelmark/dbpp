"""
Add easily ttk.Scrollbar(s) to ttk-widgets.

This is a convenience function to add scrollbars which can optionally autohide to
an existing widget which is placed already within a tk.Frame or a ttk.Frame.
  
Except for the DGScrolled function there is no function available for the DGScrolled module.  
Simply provide the  widget which should get the two scrollbars. 
The widget should be placed in its own frame before. 
Don't pack or grid the widget itself, just pack or grid the parent frame.

Examples:
 
```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.Scrolled import Scrolled
root=tk.Tk()
nframe=ttk.Frame(root)
text=tk.Text(nframe,wrap='none')
Scrolled(text)
for i in range(0,30):
   text.insert('end',"Hello very long line text ...\n")
# pack the parent frame
nframe.pack(side='top',fill='both',expand=True)
root.mainloop()
```

Copyright: @ Detlef Groth, University of Potsdam, Germany

See also: [GuiBaseClass](GuiBaseClass.html), [DGAutoScrollbar](DGAutoScrollbar.html)

License: MIT
"""

import tkinter as tk 
import tkinter.ttk as ttk
import dbpp.widgets.AutoScrollbar as AutoScrollbar

def Scrolled(widget):
    """Add autohide scrollbars to your widgets.
    
    Args:
        widget (ttk.Widget): the widget which should get scrollbars,  must be placed within a frame already
    """
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    nframe = widget.nametowidget(widget.winfo_parent())
    tsbv=AutoScrollbar.AutoScrollbar(nframe)
    tsbh=AutoScrollbar.AutoScrollbar(nframe,orient='horizontal')
    widget.configure(yscrollcommand=tsbv.set,
            xscrollcommand=tsbh.set)
    tsbv.grid(row=0, column=1, sticky='ns')
    tsbh.grid(row=1, column=0, sticky='ew')
    widget.grid(row=0, column=0, sticky='nsew')
    tsbv.config(command=widget.yview)
    tsbh.config(command=widget.xview)
    nframe.grid_rowconfigure(0, weight=1)
    nframe.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    root = tk.Tk()
    nframe=ttk.Frame(root)

    text=tk.Text(nframe,wrap='none')
    Scrolled(text)
    for i in range(0,30):
      text.insert('end',"Hello very long line text ...\n")
    mframe=ttk.Frame(root)
    tview =ttk.Treeview(mframe,columns=['col1','col2','col3'])
    tview.heading('col1',text="Column 1")
    tview.heading('col2',text="Column 2")
    tview.heading('col3',text="Column 2")
    for i in range(1,40):
        tview.insert('','end',values=[i+1,i+2,i+3])
    Scrolled(tview)
    nframe.pack(side='top',fill='both',expand=True)
    mframe.pack(side='top',fill='both',expand=True)    
    root.mainloop()

