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

<a href="../dbpp/widgets/LabEntry.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.LabEntry`
Simple composite widget of *ttk.Label* and *ttk.Entry*. 

This widget provides a simple composite widget consisting of a  *ttk.Label* and a *ttk.Entry*. At widget instantiation all arguments are forwarded to the *ttk.Entry* widget, only the option *labeltext* is forwarded to the *ttk.Label* widget as text. Subsequent changes to the widget should be performed on the  two public variables *label* and *entry*.  



**Examples:**
 

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



---

<a href="../dbpp/widgets/LabEntry.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `LabEntry`
Composite widget of ttk.Label and ttk.Entry. 

<a href="../dbpp/widgets/LabEntry.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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
