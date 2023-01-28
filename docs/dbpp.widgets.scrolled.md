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

<a href="../dbpp/widgets/scrolled.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.scrolled`
Add easily ttk.Scrollbar(s) to ttk-widgets. 

This is a convenience function to add scrollbars which can optionally autohide to an existing widget which is placed already within a tk.Frame or a ttk.Frame.  

Except for the Scrolled function there is no function available for the Scrolled module.   Simply provide the  widget which should get the two scrollbars.  The widget should be placed in its own frame before.  Don't pack or grid the widget itself, just pack or grid the parent frame. 



**Examples:**
 

```

     >>> import tkinter as tk
     >>> import tkinter.ttk as ttk
     >>> from dbpp.widgets.scrolled import Scrolled
     >>> root=tk.Tk()
     >>> nframe=ttk.Frame(root)
     >>> text=tk.Text(nframe,wrap='none')
     >>> for i in range(0,30):
     ...     text.insert('end','Hello World! In a very long line!\n')
     >>> Scrolled(text)
     >>> nframe.pack(side='top',fill='both',expand=True)
     >>> root.mainloop()

``` 

Copyright: @ Detlef Groth, 2023, University of Potsdam, Germany 

See also: [GuiBaseClass](guibaseclass.md), [AutoScrollbar](autoscrollbar.md) 

License: MIT 


---

<a href="../dbpp/widgets/scrolled.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `Scrolled`

```python
Scrolled(widget)
```

Add autohide scrollbars to your widgets. 



**Args:**
 
 - <b>`widget`</b> (ttk.Widget):  the widget which should get scrollbars,  must be placed within a frame already 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
