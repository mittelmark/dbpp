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

<a href="../dbpp/widgets/statusbar.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.statusbar`
Widget to display status information  using messages and progressbar. 

This widget provides a statusbar with Label for text message and a progressbar  to display numerical progress. 



**Examples:**
 

```

     >>> import tkinter as tk
     >>> from dbpp.widgets.statusbar import StatusBar
     >>> root = tk.Tk()
     >>> tk.Frame(root, width=200, height=100).pack()
     >>> status = StatusBar(root)
     >>> status.pack(side=tk.BOTTOM, fill=tk.X)
     >>> status.set('Connecting...')
     >>> status.progress(25)
     >>> root.update_idletasks()
     >>> root.after(1000)
     >>> root.mainloop()
     
``` 



---

<a href="../dbpp/widgets/statusbar.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `StatusBar`




<a href="../dbpp/widgets/statusbar.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(master)
```

Construct the widget within the given master widget  



**Args:**
 
 - <b>`master`</b> (ttk.Frame):  a parent widget or toplevel wherein *StatusBar* is initialized,   normally a tk.Frame or ttk.Frame widget or a Toplevel. 



**Returns:**
 StatusBar widget. 




---

<a href="../dbpp/widgets/statusbar.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `clear`

```python
clear()
```

Clears the status message. 

---

<a href="../dbpp/widgets/statusbar.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `progress`

```python
progress(n)
```

Sets the progress value (n) in the progressbar subwidget. 

---

<a href="../dbpp/widgets/statusbar.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `set`

```python
set(format, *args)
```

Sets the status message. 

Sets the message *format* into the label widget of the statusbar. Alternativly this can be a format string which will be filled with the  text string given in the *args* argument list. 



**Args:**
 


 - <b>`format`</b> (string):  text message or format string 
 - <b>`*args (list)`</b>:  variable number of arguments used as arguments for the _format_ string 






---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
