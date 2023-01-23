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

**apps:** [dbpp.peditor](dbpp.peditor.PumlEditor.md)

**[dbpp.kroki](dbpp.kroki.md) package:** 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md)

</center>

<!-- markdownlint-disable -->

<a href="../dbpp/widgets/Balloon.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.Balloon`
Basic tooltip / balloon widget using ttk.Label(s) or popups. 

This a simple tooltip implementation for displaying short help message if the mouse cursor hovers a certain widget. Such tooltips are as well called Balloon widgets. Usually tkinter comes with a tix.Ballon widget which works very similar.  However as it is often advisible to load a larger package just for using a  very small subset of its functionality here is an implementation of such a tooltip/balloon widget, which can be used instead of tix.Balloon. 



**Examples:**
 

```
import tkinter as tk
import tkinter.ttk as ttk
from dbpp.widgets.Balloon import Balloon

top=tk.Tk()
lbl1=ttk.Label(top,text="Hove me 1",anchor="center")
lbl2=ttk.Label(top,text="Hove me 2",anchor="center")
lbl3=ttk.Label(top,text="Hove me 3",anchor="center")
lbl4=ttk.Label(top,text="I am a statusbar ...",border=3,
     relief="ridge",anchor="w",padding=4)
lbl1.pack(padx=10,pady=10,fill='both',expand=True)
lbl2.pack(padx=10,pady=10,fill='both',expand=True)
lbl3.pack(padx=10,pady=10,fill='both',expand=True)
lbl4.pack(padx=3,pady=10,fill='x',expand=True,ipadx=5,ipady=5)
Balloon(lbl1,"test message 1")
Balloon(lbl2,"test message 2",background="salmon")
Balloon(lbl3," test message 3 ",timeout=0,statusbar=lbl4)
top.mainloop()
``` 

Copyright: @ Detlef Groth, University of Potsdam 

See also: [GuiBaseClass](GuiBaseClass.html) 

License: MIT 



---

<a href="../dbpp/widgets/Balloon.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `Balloon`
Tooltip/Balloon widget to display messages if widgets are hovered. 

<a href="../dbpp/widgets/Balloon.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(w, msg, timeout=2, statusbar=None, background='lightyellow')
```

Constructor method to intialize the tooltip/balloon. 

Execept for the constructor there is no method available for the Balloon class, at object instantiation  simply provide the widget and the message to be displayed.  



**Args:**
 
 - <b>`widget`</b> (ttk.Widget):  the widget to get the help message 
 - <b>`msg`</b> (string): the text message to be displayed when the mouse cursor is moved onto the widget 
 - <b>`timeout`</b> (int):  integer (seconds), the timeout thereafter the message windows will be closed, defaults to 2 
 - <b>`statusbar`</b> (ttk.Label):  an optional labelwidget on which to show the message, to supress the tooltip, give a timeout of 0, default: None 
 - <b>`background`</b> (string):  the tooltip background, defaults to 'lightyellow' 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
