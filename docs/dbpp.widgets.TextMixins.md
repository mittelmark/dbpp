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

<a href="../dbpp/widgets/TextMixins.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.TextMixins`
The module *TextMixins* adds a few small Mixin classes for the *tk.Text* widget to extend its functionality on the fly. 

The following Mixins are currently implemented: 


- TextFontIncreaserMixin - adding bindings *Ctrl-plus* and *Ctrl-minus* to change the fontsize 
- TextCuaBindingsMixin  - adds a few standard bindings like *Ctrl-a* to select the text and a status aware context menu for right mouse button clicks 
- TextHighLightMixin - a simple syntax highlighter for single and multiline comments as well as for keywords 



**Examples:**
 

```
import tkinter as tk
from dbp.widgets.TextMixins import TextMixins
root = tk.Tk()
class text(tk.Text,TextFontIncreaserMixin,TextCuaBindingsMixin,
     TextHighLightMixin): pass
txt  = text(root,undo=True) 
txt.bindTextResize()
txt.bindCua()
txt.addHighLights(commentline="'",commentstart="/'",
     commentend="'/",keywords=[ ['@startuml','@enduml'], ['class', 'entity', 'table'] ])
txt.insert("1.0","
@startuml
'This is a comment
class A
class B
A --> B
@enduml
")
txt.updateHighLights()
txt.pack(side='top',fill='both',expand=True)
root.mainloop()        
``` 



---

<a href="../dbpp/widgets/TextMixins.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `TextFontIncreaserMixin`
Adding fontsize adjustments using Ctrl-plus, Ctrl-minus to the tk.Text widget. 

Mixin class for the tk.Text widget which allows to extend its functionality on the fly by creating an empty class like this: 

```
import tkinter as tk
class MText(tk.Text,dbp.widgets.TextMixins.TextFontIncreaserMixin): pass
root = tk.Tk()
text = MText(root)
text.bindTextResize()
``` 

Now you can presse *Ctrl-Plus* to increase the font and *Ctrl-Minus* to decrease the fontsize. 




---

<a href="../dbpp/widgets/TextMixins.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `bindTextResize`

```python
bindTextResize(increase='Control-plus', decrease='Control-minus', font=None)
```

Add the actual bindings for increasing and decreasing the fontsize using the *Ctrl-Plus* and *Ctrl-Minus* keys combinations. 



**Args:**
 
 - <b>`increase`</b> (string):  the key combination to increase the fontsize, defaults to "Control-plus" 
 - <b>`decrease`</b> (string):  the key combination to decrease the fontsize, defaults to "Control-minus"             
 - <b>`font`</b> (string):  the prefered Font to be used, if not given searches for a platform depending good choice, defaults to None 

---

<a href="../dbpp/widgets/TextMixins.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `decreaseFont`

```python
decreaseFont(evt=None)
```

Decrease the font size of the widget. 

---

<a href="../dbpp/widgets/TextMixins.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `increaseFont`

```python
increaseFont(evt=None)
```

Increase the font size of the widget. 


---

<a href="../dbpp/widgets/TextMixins.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `TextCuaBindingsMixin`
CUA bindings and right click popup menu for the tk.Text widget. 

Mixin class for the tk.Text widget which allows to extend its functionality on the fly for adding standard bindings and a Right click popup menu  by creating an empty class like this: 



**Examples:**
 

```
import tkinter as tk
class MText(tk.Text,dbp.widgets.TextMixins.TextCuaBindingsMixin): pass
root = tk.Tk()
text = MText(root)
text.bindCua()
``` 

Now you can presse *Ctrl-a* for instance to select the complete text, you get as well a widget status aware context menu if you press the right mouse button in the text widget. 




---

<a href="../dbpp/widgets/TextMixins.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `bindCua`

```python
bindCua()
```

Adds the actual bindings Ctrl-x, Ctrl-c, Ctrl-v, Control-z, Control-a known as well as CUA bindings and in addition a right click context mene 


---

<a href="../dbpp/widgets/TextMixins.py#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `TextHighLightMixin`
Syntax highlighting for the tk.Text widget. 

Mixin class for the tk.Text widget which allows to extend its functionality on the fly for some minimal syntax highlighting by creating an empty class like this: 



**Example:**
 

```
import tkinter as tk
class MText(tk.Text,dbpp.widgets.TextMixins.TextHighLightMixin): pass
root = tk.Tk()
text = MText(root)
text.addHighLights(linecomment="^\s*'",keywords=[ 
     ['@startuml','@enduml', '@startmindmap','@endmindmap'], 
     ['class', 'entity', 'table'] ])
``` 




---

<a href="../dbpp/widgets/TextMixins.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `addHighLights`

```python
addHighLights(
    commentline='^\\s*#',
    commentstart=None,
    commentend=None,
    keywords=[],
    strings=True
)
```

Adds the actual syntax highlighting and the binding for updates of the high lighting after pressing Up, Down or Return. For updating after a new file is loaded see updateHighLights 



**Args:**
 
 - <b>`commentline`</b> (regex):  the regular expression to start a single line comment, defaults to "^\s*#" 
 - <b>`commentstart`</b> (regex):  the regular expression to start a multi line comment, defaults to None 
 - <b>`commentend`</b> (regex):  the regular expression to start a multie line comment, defaults to None             
 - <b>`keywords`</b> (list):  nested list of keywords, each sublist will be given a different color, defaults to list() 
 - <b>`strings`</b> (bool):  should strings be highlighted, defaults to True 



---

<a href="../dbpp/widgets/TextMixins.py#L236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `updateHighLights`

```python
updateHighLights()
```

Updates the current given syntax highlights for instance after loading a new file into the widget. If this file should support other highlighting you should before again call the method addHighLights. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
