#!/usr/bin/env python3
"""Widget to display status information  using messages and progressbar.

This widget provides a statusbar with Label for text message and a progressbar 
to display numerical progress.

Examples:

```
import tkinter as tk
from dbpp.widgets.StatusBar import StatusBar
root = tk.Tk()
tk.Frame(root, width=200, height=100).pack()
status = StatusBar(root)
status.pack(side=tk.BOTTOM, fill=tk.X)
status.set("Connecting...")
status.progress(25)
root.mainloop()
```
"""

# file StatusBar.py
import tkinter as tk
from tkinter import ttk
 

class StatusBar(ttk.Frame):
    
    def __init__(self,master):
      """Construct the widget within the given master widget
        
      Args:
          master (ttk.Frame): a parent widget or toplevel wherein *StatusBar* is initialized, 
              normally a tk.Frame or ttk.Frame widget or a Toplevel.

      Returns:
          StatusBar widget.
      """   

      ttk.Frame.__init__(self, master)
      self.label = ttk.Label(self, border=1, 
         relief='sunken', 
         anchor='w',width=50)
      self.label.pack(side='left',padx=4,pady=2,fill='x',expand=True)
      self.pb = ttk.Progressbar(self,
         length=60,mode='determinate')
      self.pb.configure(value=30)
      self.pb.pack(side='right',padx=4,pady=2)
      self.master=master

    def set(self, format, *args):
      """Sets the status message.
      
      Sets the message *format* into the label widget of the statusbar.
      Alternativly this can be a format string which will be filled with the 
      text string given in the *args* argument list.
      
      Args:

          format (string): text message or format string
          *args (list): variable number of arguments used as arguments for the _format_ string
         
      """
      self.label.config(text=format % args)
      self.master.update_idletasks()
         
    def clear(self):
      """Clears the status message."""  
      self.label.config(text="")
      self.master.update_idletasks()
      
    def progress(self,n):
      """Sets the progress value (n) in the progressbar subwidget."""
      self.pb.configure(value=n)
      self.master.update_idletasks()


if __name__ == "__main__":
  import sys
  root = tk.Tk()
  root.title('DGApp')
  ttk.Frame(root, width=200, height=100).pack()
  status = StatusBar(root)
  status.pack(side="bottom", fill="x")
  root.update()

  status.set("Connecting...")
  status.progress(25)
  #shot.shot('DGApp',root,'statusbar-python.png',ex=False)
  root.after(1000)
  status.set("Connected, logging in...")
  status.progress(50)
  root.after(1000)
  status.set("Login accepted...")
  status.progress(75)
  root.after(1000)
  status.clear()
  #sys.exit(0)
  root.mainloop()
