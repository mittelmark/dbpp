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

<a href="../dbpp/widgets/RoText.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `RoText.py`
Read only text widget. 

This is a text widget derived from the tk.Text widget where the user can't change the text. The widget otherwise has all the methods. of the original text widget. To insert text programmatically use the syntax `cmd('ins',index, text)`, to delete the text use the `cmd('del',start,end)` syntax. 





**Examples:**
 

```

     >>> import tkinter as tk
     >>> import dbpp.widgets.RoText as RoText
     >>> root= tk.Tk()   
     >>> rtext = RoText.RoText(root) 
     >>> rtext.cmd("ins","end","Hello World!")
     >>> root.title('RoTtext example')
     ''
     >>> rtext.pack(fill="both",expand=True)     

``` 

**Author:** 


- 2023 Detlef Groth 

**License:**  MIT - License 



---

## <kbd>class</kbd> `RoText`
Readonly text widget based on tkText. 

This is an wrapper for a read only text widget, based on the dgw::rotext widget. There is only one public method, `cmd` which forwards the remaining arguments to the original text widget. The widget methods insert and delete are doing nothing. To insert text you should use the `cmd` method instead. 

<a href="../dbpp/widgets/RoText.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `__init__`

```python
__init__(master=None, cnf={}, **kwargs)
```

Initialize the RoText widget. 



**Args:**
 
 - <b>`master`</b> (ttk.Frame):  the parent widget, usually a ttk.Frame, if not given the toplevel is choosen, default: None 
 - <b>`cnf, **kwargs (dict)`</b>:  options delegated to the underlying tk.Text widget  






---

<a href="../dbpp/widgets/RoText.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `cmd`

```python
cmd(cmd, *args, **kwargs)
```

Access the original methods of the tk.Text widget. 

This is the method to access all original methods of the tk.Text widget except for the `insert` and `delete` method which are disabled.  Instead of these methods you should use `w.cmd('ins', ...)` and  `w.cmd('del', ...) to insert and to delete data. 



**Args:**
 
 - <b>`cmd`</b> (string):  command of the original tk.Text widget like `configure` or `see`,  `insert` and `delete` are doing  nothing, use `ins` and `del` instead *args (list) - additional positional arguments **kwargs (dict) - additional key-value arguments 



**Example:**
 

```
    >>> import tkinter as tk
    >>> root= tk.Tk()   
    >>> rtext = RoText(root) 
    >>> rtext.cmd("ins","end","Hello World!")
    >>> rtext.get("1.0","end-1c")
    'Hello World!'
    >>> rtext.pack(fill="both",expand=True)     
    
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
