<center>

**[dbpp.widgets](dbpp.widgets.md) package:** 
[GuiBaseClass](dbpp.widgets.guibaseclass.md) -
[AutoScrollbar](dbpp.widgets.autoscrollbar.md) -
[Balloon](dbpp.widgets.balloon.md) -
[Ctext](dbpp.widgets.ctext.md) -
[LabEntry](dbpp.widgets.labentry.md) -
[RoText](dbpp.widgets.rotext.md) -
[Scrolled](dbpp.widgets.scrolled.md) -
[SqlText](dbpp.widgets.sqltext.md) -
[StatusBar](dbpp.widgets.statusbar.md) -
[TableView](dbpp.widgets.tableview.md) -
[TextMixins](dbpp.widgets.textmixins.md) -
[XTableView](dbpp.widgets.xtableview.md) -
[XTreeView](dbpp.widgets.xtreeview.md) 

[dbpp.kroki](dbpp.kroki.md) - 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.krokiencoder.md) -
[dbpp.utils](dbpp.utils.md) - 
[dbpp.utils.SqlUtils](dbpp.utils.sqlutils.md)  -

**apps:** [dbpp.peditor](dbpp.peditor.pumleditor.md)


</center>

<!-- markdownlint-disable -->

<a href="../dbpp/widgets/guibaseclass.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.guibaseclass`
Basic class on which to build Tkinter applications. 

The module *GuiBaseClass* provides an infrastructure on which you can build your own Tkinter applications. Your application should simple inheriting from that class.  The *GuiBaseClass* provides functionalities such us: 


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



**Examples:**
 

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





---

<a href="../dbpp/widgets/guibaseclass.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `GuiBaseClass`
The class to build your Tkinter applications on. 

GuiBaseClass provides has a prebuild menubar, statusbar and a mainframe to embed your own widgets, it provides further facilities to create new menu entries easily and to display messages and progress values. Methods starting with lowercase are considered to be public, can be used outside of inheriting classes, methods starting with uppercase letters such as `About` or `Exit` are considered to be protected, meanding that they should be only used within inheriting classes. 



**Attributes:**
 
 - <b>`title`</b> (str):  the application title defaults to '' 
 - <b>`author`</b> (str):  the author, defaults to '' 

<a href="../dbpp/widgets/guibaseclass.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(root=None, title='', author='')
```

Initialize the main application window within the given *root* toplevel. 




---

<a href="../dbpp/widgets/guibaseclass.py#L270"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `about`

```python
about()
```

Shows a messabox for the application. 

---

<a href="../dbpp/widgets/guibaseclass.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `add_edit_menu`

```python
add_edit_menu(target=None)
```

Add a typical Edit menu in the menubar. 

This methods adds the typical Edit menubar entry with commands like Undo, Redo, Copy, Cut etc. These entries are aware of the current status of the tk.Text widget, so if for instance Undo is not enabled, it is no available in the menu entry. 



**Args:**
 
 - <b>`target`</b> (tk.Text):  the target which for the edit operations, defaults to None 



---

<a href="../dbpp/widgets/guibaseclass.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `add_statusbar`

```python
add_statusbar()
```

Make the statusbar at the bottom visible. 

---

<a href="../dbpp/widgets/guibaseclass.py#L261"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `exit`

```python
exit(ask=True)
```

Cleanly exit the application with confirm messagebox. 



**Args:**
 
 - <b>`ask`</b> (bool):  should the confirm message box been show, defaults to True 

---

<a href="../dbpp/widgets/guibaseclass.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_frame`

```python
get_frame()
```

Get the mainframe of the application in which the user can insert its own widgets. 

---

<a href="../dbpp/widgets/guibaseclass.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_menu`

```python
get_menu(entry, **kwargs)
```

Get the given menu entry or create an new one if the requested does not exists  yet. 

This method can be used to create new menu entries in the top menubar or to extend already existing menu entries. The entries are recognized by the menu title, if an entry does not exists yet, it is created. Only in this keys the given underline option is used. 



**Args:**
  


 - <b>`entry`</b> (string):  the menu entry which should be created or returned if already existing 
 - <b>`**kwargs `</b>:  additional key value pairs, currently only underline=value is supported for new entries  



**Examples:**
 

``` 
root=tk.Tk()
bapp = GuiBaseClass(root) 
mnu=bapp.getMenu('Tools',underline=0)
mnu.add_command(label='Test',command=lambda: print('Test'))    
``` 

---

<a href="../dbpp/widgets/guibaseclass.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `message`

```python
message(msg)
```

Display the given message in the statusbar at the bottom. 

---

<a href="../dbpp/widgets/guibaseclass.py#L141"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `progress`

```python
progress(n)
```

Display the given numerical value in the progress bar at the bottom. 

---

<a href="../dbpp/widgets/guibaseclass.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `run`

```python
run()
```

Start the GUI mainloop waiting for the user to interact with the application. 

---

<a href="../dbpp/widgets/guibaseclass.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `set_app_title`

```python
set_app_title(title)
```

Sets the title of the application. 

---

<a href="../dbpp/widgets/guibaseclass.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `set_edit_target`

```python
set_edit_target(target)
```

Sets to target for the Edit menu entry to the given tk.Text widget. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
