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

<a href="../dbpp/widgets/labentry.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.labentry`
Simple composite widget of *ttk.Label* and *ttk.Entry*. 

This widget provides a simple composite widget consisting of a  *ttk.Label* and a *ttk.Entry*. At widget instantiation all arguments are forwarded to the *ttk.Entry* widget, only the option *labeltext* is forwarded to the *ttk.Label* widget as text. Subsequent changes to the widget should be performed on the  two public variables *label* and *entry*.  



**Examples:**
 

```
import tkinter as tk
import tkinter as ttk 
from dbpp.widgets.labentry import LabEntry
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

**Copyright:** Detlef Groth, 2019-2023, University of Potsdam 

**License:** MIT - License 



---

<a href="../dbpp/widgets/labentry.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `LabEntry`
Composite widget of ttk.Label and ttk.Entry. 

<a href="../dbpp/widgets/labentry.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(master, labeltext='Label:', **kwargs)
```

Constructor for the widget intializing its subwidgets. 

The widget only offers a constructor, to target the subwidgets, the ttk.Entry and the ttk.Label after creating the widget just use the public variables *self.entry* and *self.label*. 



**Args:**
 
 - <b>`master`</b> (ttk.Frame):  a parent widget or toplevel wherein the *LabEntry* widget is initialized, normally a tk.Frame or ttk.Frame widget or a Toplevel.  
 - <b>`labeltext`</b> (string):  the text for the label on the left 
 - <b>`**kwargs (dict)`</b>:  all remaining key-value arguments which are delegated to the ttk.Entry widget 



**Returns:**
 LabEntry widget with the two public components: 


 - <b>`self.label`</b>:  the ttk.Label 
 - <b>`self.entry`</b>:  the ttk.Entry 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
