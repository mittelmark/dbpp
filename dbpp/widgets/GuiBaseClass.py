#!/usr/bin/env python3
"""
Basic class on which to build Tkinter applications.

The module *GuiBaseClass* provides an infrastructure on which you can build your
own Tkinter applications. Your application should simple inheriting from that class. 
The *GuiBaseClass* provides functionalities such us:

- standard menubar with *File-Exit* and *Help-About* entries, other menus can be easily added
- an optional *Edit-Cut, Coyp, Paste* etc menu entry
- mainframe for the application in which you can add your own widgets
- status bar widget which can be shown if desired

Here an example for the basic application you get by inheriting from that class:

```{.kroki echo=false dia=ditaa}
+--------------------------------------------------+
| File | Help   cEEE       (menubar)               |
+-------------+--------------+---------------------+
|                                                  |
|               ttk.Frame                          |
|               (mainframe)                        |
|                                                  |
|                                                  |
|                                                  |
|                                                  |
|               +--StatusBar------+                |
|               |                 |                |
|               v                 v                |
+-------------------------+---------------------+--+
| ttk.Label (messages)    | ttk.Progressbar c6AA|  | 
+-------------------------+---------------------+--+
```

Examples:

```
import sys
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.gui_base_class import GuiBaseClass
bapp = GuiBaseClass() 
# example for using the BaseClass in other applications
bapp.add_edit_menu(target=None)
mnu=bapp.get_menu('Tools',underline=0)
mnu.add_command(label='Test',command=lambda: print('Test'))    

# example for using getFrame
frm=bapp.get_frame()
btn=ttk.Button(frm,text="Button X",command=lambda: sys.exit(0))
btn.pack()
txt=tk.Text(frm,undo=True)
txt.pack(side='top',fill='both',expand=True)
bapp.set_edit_target(txt)
bapp.add_statusbar()
bapp.run()
```

Here an other example where you just inherit from the *GuiBaseClass* in your own application.

```
class PumlEditor(GuiBaseClass):
    def __init__(self):
        super().__init__(root)
        self.add_statusbar()
        self.kroki = KrokiEncoder()
```

Your class then has the following dependencies:

```{.kroki dia=plantuml echo=false}
@startuml
class GuiBaseClass
class StatusBar
class PumlEditor
class KrokiEncoder

KrokiEncoder --* PumlEditor
PumlEditor -> GuiBaseClass
StatusBar --* GuiBaseClass
@enduml
```
        
"""

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
import sys
import dbpp.widgets.statusbar as sb
class GuiBaseClass():
  """The class to build your Tkinter applications on.
  
  GuiBaseClass provides has a prebuild menubar, statusbar and a mainframe to embed your
  own widgets, it provides further facilities to create new menu entries easily and to display messages
  and progress values. Methods starting with lowercase are considered to be public, can be used outside of
  inheriting classes, methods starting with uppercase letters such as `About` or `Exit` are considered to be
  protected, meanding that they should be only used within inheriting classes.
  
  Attributes:
      title (str): the application title defaults to ''
      author (str): the author, defaults to ''
  """  
  def __init__(self,root=None,title='',author=''):
      """Initialize the main application window within the given *root* toplevel."""
      # create widgets
      if root is None:
         root = tk.Tk()
      if title != '':
         self.root.title = title         
      self.root=root
      self.author = author
      self.title  = title
      self.root.option_add('*tearOff', False)
      self.menu=dict()
      self.menubar = tk.Menu(root)         
      menu_file = tk.Menu(self.menubar)
      self.menubar.add_cascade(menu=menu_file,label='File',underline=0)
      menu_file.add_separator()
      menu_file.add_command(label='Exit',  command=self.exit,underline=1)       
      menu_help = tk.Menu(self.menubar)
      self.menubar.add_cascade(menu=menu_help,label='Help',underline=0)
      menu_help.add_command(label='About', command=self.about,underline=0)       
      root.config(menu=self.menubar)
      self.menu['menubar'] = self.menubar
      self.menu['File']    = menu_file        
      self.menu['Help']    = menu_help              
      self.frame = ttk.Frame(root)
      self.frame.pack(fill='both',expand=True)
      self.status = sb.StatusBar(self.root)

  # public functions
  # methods for the StatusBar
  def add_statusbar (self):
      """Make the statusbar at the bottom visible."""
      self.status.pack(fill="x",expand=False)
      self.status.set("I am the statusbar ...")
  def message (self,msg):
      """Display the given message in the statusbar at the bottom."""
      self.status.set(msg)
  def progress(self,n):
      """Display the given numerical value in the progress bar at the bottom."""
      self.status.progress(n) 
  def run(self):
      """Start the GUI mainloop waiting for the user to interact with the application."""
      self.root.mainloop()
  def get_frame(self):
      """Get the mainframe of the application in which the user can insert its own widgets."""
      return(self.frame)  
  def get_menu(self,entry,**kwargs):
      """Get the given menu entry or create an new one if the requested does not exists  yet.
      
      This method can be used to create new menu entries in the top menubar or to extend already existing menu
      entries. The entries are recognized by the menu title, if an entry does not exists yet, it is created. Only in this keys the given underline
      option is used.
      
      Args:
          
          entry (string): the menu entry which should be created or returned if already existing
          **kwargs : additional key value pairs, currently only underline=value is supported for new entries
              
      Examples:
      
      ``` 
      root=tk.Tk()
      bapp = GuiBaseClass(root) 
      mnu=bapp.getMenu('Tools',underline=0)
      mnu.add_command(label='Test',command=lambda: print('Test'))    
      ```
      
      """
      if entry in self.menu:
        return (self.menu[entry])
      else:
        # we create a new one
        last = self.menu['menubar'].index('end')   
        self.menu[entry]= tk.Menu(self.menubar)
        self.menu['menubar'].insert_cascade(
          last, menu=self.menu[entry],label=entry)
        for key,val in kwargs.items():
            # this does not work: key=val
            if (key == "underline"):
                self.menu['menubar'].entryconfig(last,underline=val)
        return(self.menu[entry])
  def add_edit_menu(self,target=None):
      """Add a typical Edit menu in the menubar.
      
      This methods adds the typical Edit menubar entry with commands like
      Undo, Redo, Copy, Cut etc. These entries are aware of the current status
      of the tk.Text widget, so if for instance Undo is not enabled, it is no available
      in the menu entry.
      
      Args:
          target (tk.Text): the target which for the edit operations, defaults to None
          
      """    
      last = self.menu['menubar'].index('end')   
      self.menu['Edit']= tk.Menu(self.menubar)
      self.menu['menubar'].insert_cascade(
          last, menu=self.menu["Edit"],label="Edit",underline=0)
      self.menu['Edit'].add_command(label="Undo",underline=0,accelerator="Ctrl-Z")
      self.menu['Edit'].add_command(label="Redo",underline=0,accelerator="Ctrl-Shift-Z")
      self.menu['Edit'].add_separator()
      self.menu['Edit'].add_command(label="Cut",underline=1,accelerator="Ctrl-X")
      self.menu['Edit'].add_command(label="Copy",underline=0,accelerator="Ctrl-C")
      self.menu['Edit'].add_command(label="Paste",underline=0,accelerator="Ctrl-V")
      self.menu['Edit'].add_separator()
      self.menu['Edit'].add_command(label="Select All",underline=7,accelerator="Ctrl-Shift-/")
      self.edittarget=target   
      self.menu['Edit'].config(postcommand=self.__edit_select)     
      self.root.bind
  def set_edit_target(self,target):
      """Sets to target for the Edit menu entry to the given tk.Text widget."""
      self.edittarget=target   
  def set_app_title (self, title):
      """Sets the title of the application."""
      self.root.title(title)
  # private functions
  def __edit_select(self,evt=None):
      if not(self.edittarget):
        for i in range(0,self.menu['Edit'].index('end')+1):
            if (self.menu['Edit'].type(i) in ['command','radiobutton','checkbutton']):
                self.menu['Edit'].entryconfig(i,state="disabled")
      else:
        for i in range(0,self.menu['Edit'].index('end')+1):
            if (self.menu['Edit'].type(i) in ['command','radiobutton','checkbutton']):
                self.menu['Edit'].entryconfig(i,state="disabled")
            if (self.menu['Edit'].type(i) in ['command','radiobutton','checkbutton']):
                if (self.menu['Edit'].entrycget(i,"label") in ["Undo","Redo"]):
                    if self.edittarget.cget("undo") and self.edittarget.edit_modified():
                        self.menu['Edit'].entryconfig(i,state="active")
                        if (self.menu['Edit'].entrycget(i,"label") == "Undo"):
                            self.menu['Edit'].entryconfigure(i, command=lambda: self.edittarget.event_generate("<<Undo>>"))
                        else:
                            self.menu['Edit'].entryconfigure(i, command=lambda: self.edittarget.event_generate("<<Redo>>"))
                elif (self.menu['Edit'].entrycget(i,"label") in ["Cut","Copy"]):
                    if len(self.edittarget.tag_ranges('sel'))>0:
                         self.menu['Edit'].entryconfig(i,state="active")
                         if self.menu['Edit'].entrycget(i,"label") == "Cut":
                             self.menu['Edit'].entryconfigure(i, command=lambda: self.edittarget.event_generate("<<Cut>>"))
                         else:
                             self.menu['Edit'].entryconfigure(i, command=lambda: self.edittarget.event_generate("<<Copy>>"))
                elif (self.menu['Edit'].entrycget(i,"label") == "Paste"):
                    cb=""
                    try:
                        cb=self.root.selection_get(selection="CLIPBOARD")
                    except:
                        cb = ""
                    if cb != "":
                        self.menu['Edit'].entryconfigure(i, command=lambda: self.edittarget.event_generate("<<Paste>>"),state="active")
                elif (self.menu['Edit'].entrycget(i,"label") == "Select All"):
                    if len(self.edittarget.get('1.0','end')) > 1:
                        self.menu['Edit'].entryconfigure(i, command=self.__edit_target_selectAll,state="active")

  def __edit_target_select_all(self,evt=None):
        self.edittarget.tag_add('sel','1.0','end')
        # stop additional event's which might be bound to Ctrl-a 
        # like jumping cursor to the beginning of the line
        return("break")
                          
  def exit(self,ask=True):
      """Cleanly exit the application with confirm messagebox.
      
      Args:
          ask (bool): should the confirm message box been show, defaults to True
      """
      res = mbox.askyesno(title="Are you sure?",message="Really quit the application?")
      if res:
          sys.exit(0)
  def about(self):
      """Shows a messabox for the application."""
      tk.messagebox.showinfo('About', re.sub("(.+?)-?.+", "\\1",self.root.title),
            icon='info')
if __name__ == '__main__':
    root=tk.Tk()
    bapp = GuiBaseClass(root) 
    # example for using the BaseClass in other applications
    bapp.add_edit_menu(target=None)
    mnu=bapp.get_menu('Tools',underline=0)
    mnu.add_command(label='Test',command=lambda: print('Test'))
    
    # example for using getFrame
    frm=bapp.get_frame()
    btn=ttk.Button(frm,text="Button X",command=lambda: sys.exit(0))
    btn.pack()
    txt=tk.Text(frm,undo=True)
    txt.pack(side='top',fill='both',expand=True)
    bapp.set_edit_target(txt)
    bapp.add_statusbar()
    bapp.run()
