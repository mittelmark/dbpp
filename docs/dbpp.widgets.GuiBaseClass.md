<center>

**[dbpp.widgets](dbpp.widgets.md) package:** 
[GuiBaseClass](dbpp.widgets.GuiBaseClass.md) -
[AutoScrollbar](dbpp.widgets.AutoScrollbar.md) -
[Balloon](dbpp.widgets.Balloon.md) -
[Ctext](dbpp.widgets.Ctext.md) -
[LabEntry](dbpp.widgets.LabEntry.md) -
[RoText](dbpp.widgets.RoText.md) -
[Scrolled](dbpp.widgets.Scrolled.md) -
[SqlText](dbpp.widgets.SqlText.md) -
[StatusBar](dbpp.widgets.StatusBar.md) -
[TableView](dbpp.widgets.TableView.md) -
[TextMixins](dbpp.widgets.TextMixins.md) -
[XTableView](dbpp.widgets.XTableView.md) -
[XTreeView](dbpp.widgets.XTreeView.md) 

**apps:** [dbpp.peditor](dbpp.peditor.PumlEditor.md)

**[dbpp.kroki](dbpp.kroki.md) package:** 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md)

</center>

<!-- markdownlint-disable -->

<a href="../dbpp/widgets/GuiBaseClass.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `GuiBaseClass.py`
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
from dbpp.widgets.GuiBaseClass import GuiBaseClass
root=tk.Tk()
bapp = GuiBaseClass(root) 
# example for using the BaseClass in other applications
bapp.addEditMenu(target=None)
mnu=bapp.getMenu('Tools',underline=0)
mnu.add_command(label='Test',command=lambda: print('Test'))    

# example for using getFrame
frm=bapp.getFrame()
btn=ttk.Button(frm,text="Button X",command=lambda: sys.exit(0))
btn.pack()
txt=tk.Text(frm,undo=True)
txt.pack(side='top',fill='both',expand=True)
bapp.setEditTarget(txt)
bapp.addStatusBar()
bapp.mainLoop()
``` 

Here an other example where you just inherit from the *GuiBaseClass* in your own application. 

```
class PumlEditor(GuiBaseClass):
     def __init__(self,root):
         super().__init__(root)
         self.addStatusBar()
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

## <kbd>class</kbd> `GuiBaseClass`
The class to build your Tkinter applications on. 

GuiBaseClass provides has a prebuild menubar, statusbar and a mainframe to embed your own widgets, it provides further facilities to create new menu entries easily and to display messages and progress values. Methods starting with lowercase are considered to be public, can be used outside of inheriting classes, methods starting with uppercase letters such as `About` or `Exit` are considered to be protected, meanding that they should be only used within inheriting classes. 

<a href="../dbpp/widgets/GuiBaseClass.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `__init__`

```python
__init__(root)
```

Initialize the main application window within the given *root* toplevel. 




---

<a href="../dbpp/widgets/GuiBaseClass.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `About`

```python
About()
```





---

<a href="../dbpp/widgets/GuiBaseClass.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `Exit`

```python
Exit(ask=True)
```

Protected methods, to be used only in derived class, cleanly exits the application 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `addEditMenu`

```python
addEditMenu(target=None)
```

Add a typical Edit menu in the menubar. 

This methods adds the typical Edit menubar entry with commands like Undo, Redo, Copy, Cut etc. These entries are aware of the current status of the tk.Text widget, so if for instance Undo is not enabled, it is no available in the menu entry. 



**Args:**
 
 - <b>`target`</b> (tk.Text):  the target which for the edit operations, defaults to None 



---

<a href="../dbpp/widgets/GuiBaseClass.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `addStatusBar`

```python
addStatusBar()
```

Make the statusbar at the bottom visible. 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `getFrame`

```python
getFrame()
```

Get the mainframe of the application in which the user can insert its own widgets. 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L141"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `getMenu`

```python
getMenu(entry, **kwargs)
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

<a href="../dbpp/widgets/GuiBaseClass.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `mainLoop`

```python
mainLoop()
```

Start the GUI mainloop waiting for the user to interact with the application. 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `message`

```python
message(msg)
```

Display the given message in the statusbar at the bottom. 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `progress`

```python
progress(n)
```

Display the given numerical value in the progress bar at the bottom. 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `setAppTitle`

```python
setAppTitle(title)
```

Sets the title of the application. 

---

<a href="../dbpp/widgets/GuiBaseClass.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `setEditTarget`

```python
setEditTarget(target)
```

Sets to target for the Edit menu entry to the given tk.Text widget. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
