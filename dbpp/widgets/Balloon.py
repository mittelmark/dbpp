"""
Basic tooltip / balloon widget using ttk.Label(s) or popups.

This a simple tooltip implementation for displaying short help message if
the mouse cursor hovers a certain widget. Such tooltips are as well called Balloon widgets.
Usually tkinter comes with a tix.Ballon widget which works very similar. 
However as it is often advisible to load a larger package just for using a 
very small subset of its functionality here is an implementation of such a tooltip/balloon widget, which can be used instead of tix.Balloon.

Examples:

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.Balloon import DGBallon

top=tk.Tk()
lbl1=ttk.Label(top,text="Hove me 1",anchor="center")
lbl2=ttk.Label(top,text="Hove me 2",anchor="center")
lbl3=ttk.Label(top,text="Hove me 3",anchor="center")
lbl4=ttk.Label(top,text="I am a statusbar ...",border=3,
    relief="ridge",anchor="w",padding=4)
lbl1.pack(padx=10,pady=10,fill='both',expand=True)
lbl2.pack(padx=10,pady=10,fill='both',expand=True)
lbl3.pack(padx=10,pady=10,fill='both',expand=True)
lbl4.pack(padx=3,pady=10,fill='x',expand=True,ipadx=5,ipady=5)
Balloon(lbl1,"test message 1")
Balloon(lbl2,"test message 2",background="salmon")
Balloon(lbl3," test message 3 ",timeout=0,statusbar=lbl4)
top.mainloop()
```

Copyright: @ Detlef Groth, University of Potsdam

See also: [GuiBaseClass](GuiBaseClass.html)

License: MIT

"""

import tkinter as tk
import tkinter.ttk as ttk
class Balloon:
    """Tooltip/Balloon widget to display messages if widgets are hovered."""
    def __init__(self,w, msg, timeout=2,statusbar=None,background="lightyellow"):
        """Constructor method to intialize the tooltip/balloon.
        
        Execept for the constructor there is no method available for the Balloon class, at object instantiation 
        simply provide the widget and the message to be displayed. 
 
        Args:
             widget (ttk.Widget): the widget to get the help message
             msg (string):the text message to be displayed when the mouse cursor is moved onto the widget
             timeout (int): integer (seconds), the timeout thereafter the message windows will be closed, defaults to 2
             statusbar (ttk.Label): an optional labelwidget on which to show the message, to supress the tooltip, give a timeout of 0, default: None
             background (string): the tooltip background, defaults to 'lightyellow'
        """
        self._master = w
        self._msg    = msg
        #self.root   = root
        self._master.bind("<Enter>",self._onEnter)
        self._master.bind("<Leave>",self._onLeave)  
        self._timeout = timeout
        self._statusbar = statusbar
        self._background = background
    def _onEnter(self,evt):
        if self._timeout > 0:
            x, y = self._master.winfo_pointerxy()
            self._top = tk.Toplevel(bd=1)
            self._top.overrideredirect(1)
            x, y = self._master.winfo_pointerxy()    
            self._top.geometry("+{}+{}".format(x+5,y+5))
            f=tk.Frame(self._top,background=self._background)
            msgw=tk.Message(f,background=self._background,aspect=10000,borderwidth=0,
                text=self._msg,font="Helvetica 9")
            msgw.pack(padx=5,pady=5)
            f.pack()
            self._top.bind("<Button-1>",lambda: self._onClose())
            self._top.after(int(self._timeout * 1000), func=self._onClose)
        if not(type(self._statusbar) == type(None)):
            self._statusbar.configure(text=self._msg)
        #self.top.raise()

    def _onLeave(self,evt):
        self._onClose()

    def _onClose (self):
        if self._timeout > 0:
            self._top.destroy()
        if not(type(self._statusbar) == type(None)):
            self._statusbar.configure(text="")
        

if __name__ == "__main__":
    top=tk.Tk()
    lbl1=ttk.Label(top,text="Hove me 1",anchor="center")
    lbl2=ttk.Label(top,text="Hove me 2",anchor="center")
    lbl3=ttk.Label(top,text="Hove me 3",anchor="center")
    lbl4=ttk.Label(top,text="I am a statusbar ...",border=3,
        relief="ridge",anchor="w",padding=4)
    lbl1.pack(padx=10,pady=10,fill='both',expand=True)
    lbl2.pack(padx=10,pady=10,fill='both',expand=True)
    lbl3.pack(padx=10,pady=10,fill='both',expand=True)
    lbl4.pack(padx=3,pady=10,fill='x',expand=True,ipadx=5,ipady=5)
    Balloon(lbl1,"test message 1")
    Balloon(lbl2,"test message 2",background="salmon")
    Balloon(lbl3," test message 3 ",timeout=0,statusbar=lbl4)
    top.mainloop()
