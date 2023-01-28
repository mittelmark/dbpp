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

<a href="../dbpp/widgets/sqltext.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.sqltext`
SQL syntax aware text widdget with syntax highlighting 

This is a [Ctext](Ctext.html) based Text widget which supports SQL syntax for highlighting SQL code. 



**Examples:**
 

```
import tkinter as tk
from dbpp.widgets.sqltext import SqlText
root= tk.Tk()   
ctext = SqlText(root,background='gray90',border=5,relief='flat') 
root.title('SqlText example') 
ctext.pack(side='top',fill='both',expand=True)  
ctext.insert("end", "select * from sample where id == '1' or id == 'Hello'

-- a comment
 new statement
/*
c-style comment passing
 multiple lines
*/")
ctext.highlight('1.0','end')

# just sample execution on ctrl-enter
def bindExample(evt=None,widget=None):
     print(widget.get('1.0','end'))
     return("break")

ctext.bind('<Control-Return>',lambda evt: bindExample(widget=ctext))

root.mainloop()
``` 



---

<a href="../dbpp/widgets/sqltext.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `SqlText`
Python wrapper for the Tklib ctext widget which supports SQL highlighting. 

All options and methods of the Ctext widget and the tk.Text widget are supported. 

<a href="../dbpp/widgets/sqltext.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(master=None, cnf={}, **kwargs)
```

Initialize the wrapper widget. 



**Args:**
 
 - <b>`master`</b> (ttk.Frame):  the parent widget, usually a ttk.Frame, if not given the toplevel is choosen, default: None 
 - <b>`cnf, **kwargs (dict)`</b>:  options delegated to the Ctext and tk.Text widget 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
