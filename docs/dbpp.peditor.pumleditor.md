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

<a href="../dbpp/peditor/pumleditor.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `peditor.pumleditor`
Example GUI application to create diagram using the https://kroki.io webservice. 

This is an example GUI class to demostrate the following principles of object oriented programming: 


- inheritance - inheriting from GuiBaseClass 
- composition - embedding KrokiEncoder 
- mixins - including TextMixins for the tk.Text widget 

You should be able to run this application from the terminal direct if the dbpp package is installed completly using this syntax: 

 python -m dbpp.peditor ?DIAGRAMFILE?  

The filename for a diagram is optional. 

Here an image of the application: 

![](peditor.png) 


---

<a href="../dbpp/peditor/pumleditor.py#L391"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `main`

```python
main(argv)
```






---

<a href="../dbpp/peditor/pumleditor.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `text`








---

<a href="../dbpp/peditor/pumleditor.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `PumlEditor`




<a href="../dbpp/peditor/pumleditor.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(root)
```








---

<a href="../dbpp/peditor/pumleditor.py#L388"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `about`

```python
about()
```





---

<a href="../dbpp/peditor/pumleditor.py#L376"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `exit`

```python
exit()
```





---

<a href="../dbpp/peditor/pumleditor.py#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `file_insert`

```python
file_insert()
```





---

<a href="../dbpp/peditor/pumleditor.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `file_new`

```python
file_new(evt=None)
```





---

<a href="../dbpp/peditor/pumleditor.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `file_open`

```python
file_open(filename='')
```





---

<a href="../dbpp/peditor/pumleditor.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `file_save`

```python
file_save(evt=None)
```





---

<a href="../dbpp/peditor/pumleditor.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `file_save_as`

```python
file_save_as()
```





---

<a href="../dbpp/peditor/pumleditor.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_dia_type`

```python
get_dia_type()
```





---

<a href="../dbpp/peditor/pumleditor.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `image_update`

```python
image_update()
```





---

<a href="../dbpp/peditor/pumleditor.py#L237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `template_class`

```python
template_class()
```





---

<a href="../dbpp/peditor/pumleditor.py#L339"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `template_database`

```python
template_database()
```





---

<a href="../dbpp/peditor/pumleditor.py#L285"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `template_ditaa`

```python
template_ditaa()
```





---

<a href="../dbpp/peditor/pumleditor.py#L305"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `template_latex`

```python
template_latex()
```





---

<a href="../dbpp/peditor/pumleditor.py#L276"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `template_lists`

```python
template_lists(typecmd='listfonts', comment='https://plantuml.com/font')
```





---

<a href="../dbpp/peditor/pumleditor.py#L315"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `template_mindmap`

```python
template_mindmap()
```





---

<a href="../dbpp/peditor/pumleditor.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `text2url`

```python
text2url()
```





---

<a href="../dbpp/peditor/pumleditor.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `url2text`

```python
url2text()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
