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

<a href="../dbpp/kroki/KrokiEncoder.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `kroki.KrokiEncoder`
dbpp.kroki.KrokiEncoder - class to encode diagram code as krokio.io URL's and to decode   them back to text. 

This class provides methods to convert diagram code for tools like  [PlantUML](https://plantuml.com), [GraphViz](https://www.graphviz.org) or [Ditaa](https://ditaa.sourceforge.net/) to base64 encoded URL's ready to display  them as web images using the [https://kroki.io](https://kroki.io) and ready to edit them online using the [Niolesk web editor](https://niolesk.top/). 



**Examples:**
 

```python
from dbpp.kroki.KrokiEncoder import KrokiEncoder
kroki = KrokiEncoder()
kroki.text2kroki("A --> B")
kroki.text2kroki("class A { }",dia='plantuml',ext='svg')  
kroki.dia2kroki('input.pml',dia='plantuml',ext='png')
```      

Classes: 

```{.kroki echo=false dia=plantuml}
@startuml
class A
class B

A ->  B
@enduml
``` 

```
     >>> x = 1
     >>> x + 1
     2
     >>> from dbpp.kroki.KrokiEncoder import KrokiEncoder
     >>> kroki = KrokiEncoder()
     >>> kroki.text2kroki("class A { }",dia='plantuml',ext='svg')  
     'https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA=='
```  

## DOCUMENTATION 


---

<a href="../dbpp/kroki/KrokiEncoder.py#L253"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `usage`

```python
usage(args)
```

Usage information for the KrokiEncoder as a standalone application." 



**Args:**
 
 - <b>`args`</b> (list):  argument list in order: appname, filename, dia, ext 


---

<a href="../dbpp/kroki/KrokiEncoder.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `main`

```python
main(args)
```

Starting the KrokiEncoder as standalone application using command line options. Can  be directly called programatically like this: 



**Args:**
 
 - <b>`args`</b> (list):  argument list in order: appname, filename, dia, ext 

```
import KrokiEncoder
KrokiEncoder.main([None,'diagram.pml','plantuml','png'])
``` 

Here an example for converting a PlantUML file into a PNG image using the command line  application interface: 

```
$ KrokiEncoder.py diagram.pml plantuml png
``` 

Thereafter the file ```diagram.png``` should be in parallel to the file ``diagram.pml``. 

here a file ``diagram.pml`` with the following content and below the output: 

```{.kroki dia=plantuml}
@startuml
class A {
    var1
    method1()
}
class B {
    var2
    method2()
}
A -> B
@enduml
```   


---

<a href="../dbpp/kroki/KrokiEncoder.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `KrokiEncoder`
Class to encode and decode diagram code using the  [https://kroki.io](https://kroki.io) web service. 

Here the methods of the class: 

```{.kroki echo=false dia=plantuml}
@startuml
class KrokiEncoder { 
     dia2file()
     dia2kroki()
     kroki2dia()
     text2kroki()
}
@enduml
```  






---

<a href="../dbpp/kroki/KrokiEncoder.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `dia2file`

```python
dia2file(diafile, dia='ditaa', ext='png', imagefile='')
```

Converts a diagram file to an image file. 



**Args:**
 
 - <b>`diafile`</b> (string):  a diagram file, for instance with the pml extension for   PlantUML code, defaults to None 
 - <b>`dia`</b> (string):  diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz',   defaults to 'ditaa' 
 - <b>`ext`</b> (string):  file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,  defaults to 'png' 
 - <b>`imagefile`</b> (string):  a output filename for the image file, if not given the diagram  imagefile will have the basename of the diagram file nut with the image extension. 

**Returns:**
 None 

---

<a href="../dbpp/kroki/KrokiEncoder.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `dia2kroki`

```python
dia2kroki(filename, dia='ditaa', ext='png')
```

Converts a diagram file to a Kroki URL 



**Args:**
 
 - <b>`filename`</b> (string):  a diagram file, for instance with the pml extension for   PlantUML code, defaults to None 
 - <b>`dia`</b> (string):  diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz',   defaults to 'ditaa' 
 - <b>`ext`</b> (string):  file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,  defaults to 'png' 

**Returns:**
 Kroki-URL (string) 

---

<a href="../dbpp/kroki/KrokiEncoder.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `kroki2dia`

```python
kroki2dia(url)
```

Converts a Kroki URL back to diagram code. 



**Args:**
 
 - <b>`url`</b> (string):  a kroki URL like https://kroki.io/plantuml/svg/eNpLzkksLlZwVOBKBjOcoLQzl6OCrhaQ66Sga6fgDADcPwn7,  defaults to None 

**Returns:**
 diagram code (string) 



**Examples:**
 

```{.py echo=true}
import sys, os
sys.path.append(os.path.join(os.getcwd(),".."))
from KrokiEncoder import KrokiEncoder
kroki=KrokiEncoder()
text=kroki.kroki2dia('https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqOXiSgZznCAcRwVdLQUnAJ-uCKI=')
print(text)
``` 

---

<a href="../dbpp/kroki/KrokiEncoder.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `text2kroki`

```python
text2kroki(text, dia='ditaa', ext='png')
```

Converts a given diagram text to a Kroki URL. 



**Args:**
 
 - <b>`text`</b> (string):  diagram text as string, for instance PlantUML   code, defaults to None 
 - <b>`dia`</b> (string):  diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz',   defaults to 'ditaa' 
 - <b>`ext`</b> (string):  file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,  defaults to 'png' 

**Returns:**
 Kroki-URL (string) 






---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
