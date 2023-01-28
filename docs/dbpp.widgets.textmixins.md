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

<a href="../dbpp/widgets/textmixins.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `textmixins.py`
The module *TextMixins* adds a few small Mixin classes for the *tk.Text* widget to extend its functionality on the fly. 

The following Mixins are currently implemented: 


- TextFontIncreaserMixin - adding bindings *Ctrl-plus* and *Ctrl-minus* to change the fontsize 
- TextCuaBindingsMixin  - adds a few standard bindings like *Ctrl-a* to select the text and a status aware context menu for right mouse button clicks 
- TextHighLightMixin - simple syntax highlighter for single and multiline comments as well as for keywords 



**Examples:**
 

```

     >>> import tkinter as tk
     >>> import dbpp.widgets.textmixins as txm
     >>> root = tk.Tk()
     >>> class text(tk.Text,
     ...    txm.TextFontIncreaserMixin,
     ...    txm.TextCuaBindingsMixin,
     ...    txm.TextHighLightMixin): pass
     >>> txt  = text(root,undo=True) 
     >>> txt.bind_text_resize()
     >>> txt.bind_cua()
     >>> txt.add_highlights(commentline="'",commentstart="/'",
     ...    commentend="'/",keywords=[ ['@startuml','@enduml'], ['class', 'entity', 'table'] ])
     >>> txt.insert("1.0","@startuml\n'This is a comment\nclass A\nclass B\nA --> B\n@enduml\n")
     >>> txt.update_highlights()
     >>> txt.pack(side='top',fill='both',expand=True)
     >>> root.mainloop()        

``` 



---

## <kbd>class</kbd> `TextCuaBindingsMixin`
CUA bindings and right click popup menu for the tk.Text widget. 

Mixin class for the tk.Text widget which allows to extend its functionality on the fly for adding standard bindings and a Right click popup menu  by creating an empty class like this: 



**Examples:**
 

```
import tkinter as tk
class MText(tk.Text,dbpp.widgets.TextMixins.TextCuaBindingsMixin): pass
root = tk.Tk()
text = MText(root)
text.bind_cua()
``` 

Now you can presse *Ctrl-a* for instance to select the complete text, you get as well a widget status aware context menu if you press the right mouse button in the text widget. 




---

<a href="../dbpp/widgets/textmixins.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `bind_cua`

```python
bind_cua()
```

Adds the actual bindings Ctrl-x, Ctrl-c, Ctrl-v, Control-z, Control-a known as well as CUA bindings and in addition a right click context mene 


---

## <kbd>class</kbd> `TextFontIncreaserMixin`
Adding fontsize adjustments using Ctrl-plus, Ctrl-minus to the tk.Text widget. 

Mixin class for the tk.Text widget which allows to extend its functionality on the fly by creating an empty class like this: 

```
import tkinter as tk
class MText(tk.Text,dbpp.widgets.TextMixins.TextFontIncreaserMixin): pass
root = tk.Tk()
text = MText(root)
text.bindTextResize()
``` 

Now you can presse *Ctrl-Plus* to increase the font and *Ctrl-Minus* to decrease the fontsize. 




---

<a href="../dbpp/widgets/textmixins.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `bind_text_resize`

```python
bind_text_resize(increase='Control-plus', decrease='Control-minus', font=None)
```

Add the actual bindings for increasing and decreasing the fontsize using the *Ctrl-Plus* and *Ctrl-Minus* keys combinations. 



**Args:**
 
 - <b>`increase`</b> (string):  the key combination to increase the fontsize, defaults to "Control-plus" 
 - <b>`decrease`</b> (string):  the key combination to decrease the fontsize, defaults to "Control-minus"             
 - <b>`font`</b> (string):  the prefered Font to be used, if not given searches for a platform depending good choice, defaults to None 

---

<a href="../dbpp/widgets/textmixins.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `decrease_font`

```python
decrease_font(evt=None)
```

Decrease the font size of the widget. 

---

<a href="../dbpp/widgets/textmixins.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `increase_font`

```python
increase_font(evt=None)
```

Increase the font size of the widget. 


---

## <kbd>class</kbd> `TextHighLightMixin`
Syntax highlighting for the tk.Text widget. 

Mixin class for the tk.Text widget which allows to extend its functionality on the fly for some minimal syntax highlighting by creating an empty class like this: 



**Example:**
 

```
import tkinter as tk
class MText(tk.Text,dbpp.widgets.TextMixins.TextHighLightMixin): pass
root = tk.Tk()
text = MText(root)
text.add_highlights(linecomment="^\s*'",keywords=[ 
     ['@startuml','@enduml', '@startmindmap','@endmindmap'], 
     ['class', 'entity', 'table'] ])
``` 




---

<a href="../dbpp/widgets/textmixins.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `add_highlights`

```python
add_highlights(
    commentline='^\\s*#',
    commentstart=None,
    commentend=None,
    keywords=[],
    strings=True
)
```

Adds the actual syntax highlighting and the binding for updates of the high lighting after pressing Up, Down or Return. For updating after a new file is loaded see update_highlights 



**Args:**
 
 - <b>`commentline`</b> (regex):  the regular expression to start a single line comment, defaults to "^\s*#" 
 - <b>`commentstart`</b> (regex):  the regular expression to start a multi line comment, defaults to None 
 - <b>`commentend`</b> (regex):  the regular expression to start a multie line comment, defaults to None             
 - <b>`keywords`</b> (list):  nested list of keywords, each sublist will be given a different color, defaults to list() 
 - <b>`strings`</b> (bool):  should strings be highlighted, defaults to True 



---

<a href="../dbpp/widgets/textmixins.py#L234"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `update_highlights`

```python
update_highlights()
```

Updates the current given syntax highlights for instance after loading a new file into the widget. If this file should support other highlighting you should before again call the method addHighLights. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
