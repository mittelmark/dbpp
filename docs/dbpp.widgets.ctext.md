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

<a href="../dbpp/widgets/ctext.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `widgets.ctext`
Python wrapper for the Tklib ctext widget. 

This is a text widget derived from the tk.Text widget with support for syntax highlighting and line numbers. 

See the Tk documentation for complete details of the use of this widget [here](https://core.tcl-lang.org/tklib/doc/trunk/embedded/md/tklib/files/modules/ctext/ctext.md). 



**Examples:**
 

```
import tkinter as tk
import dbpp.widget.ctext as Ctext
root= tk.Tk()   
ctext = Ctext(root) 
ctext.add_highlight_class('DML1', 'blue', ['select','SELECT','from','FROM'])
ctext.add_highlight_class('DML2', 'blue', ['and', 'AND', 'as','AS', 'or', 'OR'])
ctext.add_highlight_class('functions','OrangeRed3',  ['avg', 'AVG', 'count','COUNT']),          
ctext.add_highlight_chars('math operators', 'magenta',  ['*','>','<','='])      
ctext.add_highlight_regexp("comment","dark green", "--.+")
ctext.add_highlight_regexp("string","magenta", "['"].+?['"]")
ctext.enable_c_comments(True)

ctext.tag_configure('_cComment',foreground="dark green")
root.title('Ctext example') 
ctext.pack()    
ctext.insert("end", "select * from sample where id == '1' or id == "Hello"

-- a comment
 new statement
/*
c-style comment passing
 multiple lines
*/")
ctext.highlight('1.0','end')
ctext.mainloop()
``` 

**Authors:** 


- 2017 Pat Thoyts 
- 2020-2023 Detlef Groth 

**License:**  MIT - License 



---

<a href="../dbpp/widgets/ctext.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `Ctext`
Python wrapper for the Tklib ctext widget 



**Attributes:**
 
 - <b>`highlight`</b> (bool):  Takes a boolean value which defines whether or not to highlight text which is inserted or deleted. The default is True 
 - <b>`linemap`</b> (bool):  line numbers left of the text widget, defaults to True 
 - <b>`linemapbg`</b> (string):  background color of the linemap, default is like in the text widget 
 - <b>`linemapfg`</b> (string):  foreground color of the linemap, default is like in the text widget 
 - <b>`linemap_select_fg`</b> (string):  Changes the selected line foreground. The default is black. 
 - <b>`linemap_select_bg`</b> (string):  Changes the selected line background. The default is yellow. 
 - <b>`linemap_mark_command`</b> (string):  Calls a procedure or command with the pathName of the ctext window, the type which is either marked or unmarked, and finally the line number selected. The proc prototype is: `linemark_cmd (win, type, line) 
 - <b>`linemap_markable`</b> (bool):  Takes a boolean value which specifies whether or not lines in the linemap are markable with the mouse. The default is True. 

<a href="../dbpp/widgets/ctext.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(master=None, cnf={}, **kwargs)
```

Initialize the ctext wrapper. 



**Args:**
 
 - <b>`master`</b> (ttk.Frame):  the parent widget, usually a ttk.Frame, if not given the toplevel is choosen, default: None 
 - <b>`cnf, **kwargs (dict)`</b>:  options delegated to the ctext widget  






---

<a href="../dbpp/widgets/ctext.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `add_highlight_chars`

```python
add_highlight_chars(classname, color, chars)
```

Add a highlighting class that matches any of the characters contained in `chars`. 



**Args:**
 
 - <b>`classname`</b> (string):  a classname used as text tag internally 
 - <b>`color`</b> (string):  a color used for highlighting 
 - <b>`chars`</b> (list):  list of single characters for highlighting text which comes after that char 

---

<a href="../dbpp/widgets/ctext.py#L115"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `add_highlight_class`

```python
add_highlight_class(classname, color, wordlist)
```

Add a highlighting class `classname` to the widget using the given color containing all the words in the `wordlist`. 



**Args:**
 
 - <b>`classname`</b> (string):  a classname used as text tag internally 
 - <b>`color`</b> (string):  a color used for highlighting 
 - <b>`wordlist`</b> (string):  a list of keywords, case sensitive 

---

<a href="../dbpp/widgets/ctext.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `add_highlight_prefix`

```python
add_highlight_prefix(classname, color, char)
```

Add a highlighting class that matches any word that starts with the specified `char`. 



**Args:**
 
 - <b>`classname`</b> (string):  a classname used as text tag internally 
 - <b>`color`</b> (string):  a color used for highlighting 
 - <b>`char`</b> (chr):  a single character for highlighting text which comes after that char 

---

<a href="../dbpp/widgets/ctext.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `add_highlight_regexp`

```python
add_highlight_regexp(classname, color, pattern)
```

Add a highlighting class that matches a regular expression to apply the chosen color. 

**Args:**
 
 - <b>`classname`</b> (string):  a classname used as text tag internally 
 - <b>`color`</b> (string):  a color used for highlighting 
 - <b>`pattern`</b> (regex):  a regular expression used for for highlighting text 

---

<a href="../dbpp/widgets/ctext.py#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `append`

```python
append()
```

Append the selected text from this widget to the clipboard. 

---

<a href="../dbpp/widgets/ctext.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `clear_highlight_classes`

```python
clear_highlight_classes()
```

Remove all highlight classes from this widget. 

---

<a href="../dbpp/widgets/ctext.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `copy`

```python
copy()
```

Copy the selected text from this widget to the clipboard. 

---

<a href="../dbpp/widgets/ctext.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `cut`

```python
cut()
```

Copy the selected text from this widget to the clipboard and then delete it from the widget. 

---

<a href="../dbpp/widgets/ctext.py#L163"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `delete_highlight_class`

```python
delete_highlight_class(classname)
```

Delete the selected highlight class from the widget. 

---

<a href="../dbpp/widgets/ctext.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `enable_c_comments`

```python
enable_c_comments(enable)
```

Enable C comment highlighting. 

The class for c-style comments is `_cComment`. This highlighting is disabled by default. 



**Args:**
 
 - <b>`enable`</b> (bool):  if True C comments are enabled 

---

<a href="../dbpp/widgets/ctext.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fastdelete`

```python
fastdelete(index, index2=None)
```

Delete the text range specified without updating the highlighting. Arguments are identical to the delete method. 

---

<a href="../dbpp/widgets/ctext.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fastinsert`

```python
fastinsert(index, *args)
```

Insert text without updating the highlighting. Arguments are identical to the insert method. 

---

<a href="../dbpp/widgets/ctext.py#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_highlight_classes`

```python
get_highlight_classes()
```

Return a list of all the highlight class names defined for this widget. 

---

<a href="../dbpp/widgets/ctext.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `highlight`

```python
highlight(start_index, end_index)
```

Highlight the text between start_index and end_index. 

---

<a href="../dbpp/widgets/ctext.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `paste`

```python
paste()
```

Paste the contents of the clipboard to the insertion point of the ctext widget. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
