"""
Simple composite widget of *ttk.Label* and *ttk.Entry*.

This widget provides a simple composite widget consisting of a 
*ttk.Label* and a *ttk.Entry*. At widget instantiation all arguments are forwarded
to the *ttk.Entry* widget, only the option *labeltext* is forwarded to the *ttk.Label*
widget as text. Subsequent changes to the widget should be performed on the 
two public variables *label* and *entry*. 

Examples:
 
```
import tkinter as tk
import tkinter as ttk 
from dbpp.widgets.LabEntry import LabEntry
root = tk.Tk()
var=tk.StringVar()
var.set("Hello")
dgl1=LabEntry(root, labeltext="This",textvariable=var)
passw=tk.StringVar()
passw.set("secret-0815")
dgl2=LabEntry(root, labeltext="Password",textvariable=passw,show="*")  
dgl1.pack(side='top',fill="x",expand=True)
dgl2.pack(side='top',fill="x",expand=True)  
dgl2.label.configure(foreground="red")
root.mainloop()
```

**Copyright:** Detlef Groth, University of Potsdam, 2019-2023

**License:** MIT - License

"""
# file StatusBar.py
import tkinter as tk
import tkinter.ttk as ttk

#'
#' <a name="command"> </a> 
#' ## COMMAND
#'
#' **LabEntry(master,labeltext=text,**kwargs)**
#'
#' > *Arguments:*
#'
#' 
class LabEntry(ttk.Frame):
    """Composite widget of ttk.Label and ttk.Entry."""
    def __init__(self,master,labeltext="Label:", **kwargs):
      """Constructor for the widget intializing its subwidgets.
      
      The widget only offers a constructor, to target the subwidgets, the ttk.Entry
      and the ttk.Label after creating the widget just use the public variables *self.entry* and *self.label*.
      
      Args:
          master (ttk.Frame): a parent widget or toplevel wherein the *LabEntry* widget is initialized, normally a tk.Frame or ttk.Frame widget or a Toplevel. 
          labeltext (string): the text for the label on the left
          **kwargs (dict): all remaining key-value arguments which are delegated to the ttk.Entry widget

      Returns:  
          LabEntry widget with the two public components:
          
          self.label: the ttk.Label
          self.entry: the ttk.Entry
      """
      ttk.Frame.__init__(self, master)
      self.label = ttk.Label(self, text=labeltext, anchor='w',width=20,padding=1)
      self.label.pack(side='left',padx=4,pady=2)
      self.entry = ttk.Entry(self,**kwargs)
      self.entry.pack(side='left',padx=4,pady=2,expand=True,fill='x')
if __name__ == "__main__":
  root = tk.Tk()
  root.title('DGApp')
  var=tk.StringVar()
  var.set("Hello")
  dgl1=LabEntry(root, labeltext="This",textvariable=var)
  passw=tk.StringVar()
  passw.set("secret-0815")
  dgl2=LabEntry(root, labeltext="Password",textvariable=passw,show="*")  
  dgl1.pack(side='top',fill="x",expand=True)
  dgl2.pack(side='top',fill="x",expand=True)  
  dgl2.label.configure(foreground="red")
  root.mainloop()

   
