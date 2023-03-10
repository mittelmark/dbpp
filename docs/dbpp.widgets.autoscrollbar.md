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

<a href="../dbpp/widgets/autoscrollbar.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.autoscrollbar`
Provides ttk.Scrollbars for widgets with autohide functionality if not needed. 

This a scrollbar which will hide itself if the widget for which they are configured do not acutally need scrollbars, for instance a text widget, where the current geometry is large enought to display all text. The widget and the the scrollbars will be gridded within the same geometry manager,  so it usually required to place the scrollbars and the widget into the same frame without other widgets.  **This widget requires some effort to create scollbars, if you just like to have a simpler procedure  to add those scrollbars use the [Scrolled](dbpp.widgets.scrolled.md) method.** 



**Examples:**
 

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.autoscrollbar import AutoScrollbar
root=tk.Tk()
nframe=ttk.Frame(root)
tsbv=AutoScrollbar(nframe)
tsbh=AutoScrollbar(nframe,orient='horizontal')
text=tk.Text(nframe,
     yscrollcommand=tsbv.set,
     xscrollcommand=tsbh.set,wrap="none")
tsbv.grid(row=0, column=1, sticky='ns')
tsbh.grid(row=1, column=0, sticky='ew')
text.grid(row=0, column=0, sticky='nsew')
tsbv.config(command=text.yview)
tsbh.config(command=text.xview)
for i in range(0,30):
     text.insert('end',"Hello Text ...
")

nframe.grid_rowconfigure(0, weight=1)
nframe.grid_columnconfigure(0, weight=1)
nframe.pack(side='top',fill='both',expand=True)
root.mainloop()
```  

Copyright: @ Detlef Groth, 2023, Caputh-Schwielowsee  



See also: [Scrolled](scrolled.md) which provides an easier interface to this widget. 

License: MIT 



---

<a href="../dbpp/widgets/autoscrollbar.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `AutoScrollbar`
Provides scrollbars for tkinter widgets which are hidden if not needed. 

Except for the constructor there is no method available for the AutoScrollbar class, at object instantiation.  Simply provide the parent widget as usually and the standard arguments for ttk.Scrollbars. Only works if the target widget is managed by grid. 

<a href="../dbpp/widgets/autoscrollbar.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent, *args, **kwargs)
```

Constructor for AutoScrollbar giving the parent widget where to place the scrollbar. 



**Args:**
 
 - <b>`parent`</b> (ttk.Widget):  the parent widget wherein the scrollbar will be added 
 - <b>`*args (list)`</b>:  additional list arguments, usually not used 
 - <b>`**kwargs (dict)`</b>:  standard ttk.Scrollbar arguments which will be delegated to the ttk.Scrollbar, usually not used 




---

<a href="../dbpp/widgets/autoscrollbar.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `pack`

```python
pack(**kw)
```

Method should be not called directly. 

---

<a href="../dbpp/widgets/autoscrollbar.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `place`

```python
place(**kw)
```

Method should be not called directly. 

---

<a href="../dbpp/widgets/autoscrollbar.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `set`

```python
set(lo, hi)
```

Method should be not called directly. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
