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

[dbpp.kroki](dbpp.kroki.md) - 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md) -
[dbpp.utils](dbpp.utils.md) - 
[dbpp.utils.SqlUtils](dbpp.utils.SqlUtils.md)  -

**apps:** [dbpp.peditor](dbpp.peditor.PumlEditor.md)


</center>

<!-- markdownlint-disable -->

<a href="../dbpp/widgets/TableView.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.TableView`
Table widget based on ttk.Treeview with scrollbars shown if needed.  

This a widget to display tabular data using the standard ttk.Treeview widget,  inheriting all its methods and options. Further the widget has automatically shown or hidden scrollbars.  A convenience function to load tabular data is implemented as well. 



**Examples:**
 

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.TableView import TableView 
root = tk.Tk()
root.title('TableView demo')
dgtab=TableView(root)
dgtab.pack(side='top',fill='both',expand=True)
dgtab.readTabfile("iris.tab")
```  

**Author:** Detlef Groth, University of Potsdam, 2019-2023 

**License:** MIT - License 



---

<a href="../dbpp/widgets/TableView.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `TableView`




<a href="../dbpp/widgets/TableView.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent, *args, **kwargs)
```

The constructor to create a TableView widget. 



**Args:**
 
 - <b>`parent`</b> (ttk.Frame): the parent widget wherein the ttk.Treeview widget will be placed. 
 - <b>`*args (list)`</b>:  standard ttk.Treeview arguments which will be delegated to the widget 
 - <b>`**kwargs (dict)`</b>:  standard ttk.Treeview arguments which will be delegated to the widget 



**Returns:**
 TableView widget with addtional methods and all methods of a ttk.Treeview widget 




---

<a href="../dbpp/widgets/TableView.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `readTabfile`

```python
readTabfile(filename)
```

Reads a tabular formatted data file and displays it into the `TableView` widget. 



**Args:**
 
 - <b>`filename`</b> (string):  the name of a tabular file 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
