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

<a href="../dbpp/widgets/StatusBar.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.StatusBar`
Widget to display status information  using messages and progressbar. 

This widget provides a statusbar with Label for text message and a progressbar  to display numerical progress. 



**Examples:**
 

```
import tkinter as tk
from dbpp.widgets.StatusBar import StatusBar
root = tk.Tk()
tk.Frame(root, width=200, height=100).pack()
status = StatusBar(root)
status.pack(side=tk.BOTTOM, fill=tk.X)
status.set("Connecting...")
status.progress(25)
root.mainloop()
``` 



---

<a href="../dbpp/widgets/StatusBar.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `StatusBar`




<a href="../dbpp/widgets/StatusBar.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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

<a href="../dbpp/widgets/StatusBar.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `clear`

```python
clear()
```

Clears the status message. 

---

<a href="../dbpp/widgets/StatusBar.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `progress`

```python
progress(n)
```

Sets the progress value (n) in the progressbar subwidget. 

---

<a href="../dbpp/widgets/StatusBar.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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
