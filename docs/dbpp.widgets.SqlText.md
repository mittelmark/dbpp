<center>
**[dbpp.widgets](dbpp.widgets.md) package:** 
[GuiBaseClass](dbpp.widgets.GuiBaseClass.md) -
[AutoScrollbar](dbpp.widgets.AutoScrollbar.md) -
[Balloon](dbpp.widgets.Balloon.md) -
[Ctext](dbpp.widgets.Ctext.md) -
[LabEntry](dbpp.widgets.LabEntry.md) -
[Scrolled](dbpp.widgets.Scrolled.md) -
[SqlText](dbpp.widgets.SqlText.md) -
[StatusBar](dbpp.widgets.StatusBar.md) -
[TableView](dbpp.widgets.TableView.md) -
[TextMixins](dbpp.widgets.TextMixins.md) -
[XTableView](dbpp.widgets.XTableView.md) -
[XTreeView](dbpp.widgets.XTreeView.md) 

**[dbpp.kroki](dbpp.kroki.md) package:** 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md)
</center>

<!-- markdownlint-disable -->

<a href="../dbpp/widgets/SqlText.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.SqlText`
SQL syntax aware text widdget with syntax highlighting 

This is a [Ctext](Ctext.html) based Text widget which supports SQL syntax for highlighting SQL code. 



**Examples:**
 

```
import tkinter as tk
from dbpp.widgets.SqlText import SqlText
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

<a href="../dbpp/widgets/SqlText.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `SqlText`
Python wrapper for the Tklib ctext widget which supports SQL highlighting. 

All options and methods of the Ctext widget and the tk.Text widget are supported. 

<a href="../dbpp/widgets/SqlText.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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
