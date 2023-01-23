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

<a href="../dbpp/widgets/Scrolled.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.Scrolled`
Add easily ttk.Scrollbar(s) to ttk-widgets. 

This is a convenience function to add scrollbars which can optionally autohide to an existing widget which is placed already within a tk.Frame or a ttk.Frame.  

Except for the DGScrolled function there is no function available for the DGScrolled module.   Simply provide the  widget which should get the two scrollbars.  The widget should be placed in its own frame before.  Don't pack or grid the widget itself, just pack or grid the parent frame. 



**Examples:**
 

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.Scrolled import Scrolled
root=tk.Tk()
nframe=ttk.Frame(root)
text=tk.Text(nframe,wrap='none')
Scrolled(text)
for i in range(0,30):
    text.insert('end',"Hello very long line text ...
")
# pack the parent frame
nframe.pack(side='top',fill='both',expand=True)
root.mainloop()
``` 

Copyright: @ Detlef Groth, University of Potsdam, Germany 

See also: [GuiBaseClass](GuiBaseClass.html), [DGAutoScrollbar](DGAutoScrollbar.html) 

License: MIT 


---

<a href="../dbpp/widgets/Scrolled.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `Scrolled`

```python
Scrolled(widget)
```

Add autohide scrollbars to your widgets. 



**Args:**
 
 - <b>`widget`</b> (ttk.Widget):  the widget which should get scrollbars,  must be placed within a frame already 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
