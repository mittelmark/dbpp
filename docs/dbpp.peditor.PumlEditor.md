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

<a href="../dbpp/peditor/PumlEditor.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `peditor.PumlEditor`
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

<a href="../dbpp/peditor/PumlEditor.py#L389"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `main`

```python
main(argv)
```






---

<a href="../dbpp/peditor/PumlEditor.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `text`








---

<a href="../dbpp/peditor/PumlEditor.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `PumlEditor`




<a href="../dbpp/peditor/PumlEditor.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(root)
```








---

<a href="../dbpp/peditor/PumlEditor.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `ImageUpdate`

```python
ImageUpdate()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fileInsert`

```python
fileInsert()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fileNew`

```python
fileNew(evt=None)
```





---

<a href="../dbpp/peditor/PumlEditor.py#L136"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fileOpen`

```python
fileOpen(filename='')
```





---

<a href="../dbpp/peditor/PumlEditor.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fileSave`

```python
fileSave(evt=None)
```





---

<a href="../dbpp/peditor/PumlEditor.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `fileSaveAs`

```python
fileSaveAs()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `getDiaType`

```python
getDiaType()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L235"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `templateClass`

```python
templateClass()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L337"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `templateDatabase`

```python
templateDatabase()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L283"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `templateDitaa`

```python
templateDitaa()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L303"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `templateLaTeX`

```python
templateLaTeX()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L274"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `templateLists`

```python
templateLists(typecmd='listfonts', comment='https://plantuml.com/font')
```





---

<a href="../dbpp/peditor/PumlEditor.py#L313"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `templateMindmap`

```python
templateMindmap()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `text2url`

```python
text2url()
```





---

<a href="../dbpp/peditor/PumlEditor.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `url2text`

```python
url2text()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
