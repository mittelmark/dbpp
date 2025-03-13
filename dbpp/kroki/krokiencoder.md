<center>
    [mkdoc](../mkdoc/mkdoc.md) -
    [pydoc2md](../pydoc2md/pydoc2md.md) -
    [krokiencoder](../kroki/krokiencoder.md)
</center>
## dbpp.kroki.KrokiEncoder 

Class to encode diagram code as https://krokio.io URL's and to decode 
them back to text.

This class provides methods to convert diagram code for tools like 
[PlantUML](https://plantuml.com), [GraphViz](https://www.graphviz.org) or
[Ditaa](https://ditaa.sourceforge.net/) to base64 encoded URL's ready to display 
them as web images using the [https://kroki.io](https://kroki.io) and ready to edit them online
 using the [Niolesk web editor](https://niolesk.top/).

Examples:

```python
from dbpp.kroki.krokiencoder import KrokiEncoder
kroki = KrokiEncoder()
kroki.text2kroki("A --> B")
kroki.text2kroki("class A { }",dia='plantuml',ext='svg')  
kroki.dia2kroki('input.pml',dia='plantuml',ext='png')
```     

Classes:

```
@startuml
class A
class B

A ->  B
@enduml

```
![](https://kroki.io/plantuml/png/eNpzKC5JLCopzc3hSs5JLC5WcITSTlxcjgq6dgpAhkNqXgpIAQA1mgz7)

```
    >>> x = 1
    >>> x + 1
    2
    >>> from dbpp.kroki.krokiencoder import KrokiEncoder
    >>> kroki = KrokiEncoder()
    >>> kroki.text2kroki("class A { }",dia='plantuml',ext='svg')  
    'https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA=='
```


## Class: krokiencoder.KrokiEncoder

Class to encode and decode diagram code using the 
[https://kroki.io](https://kroki.io) web service.

Here the methods of the class:

![](https://kroki.io/plantuml/png/eNpTUFBQcCguSSwqKc3N4QJyFJJzEouLFbyL8rMzXfOS81NSixSqFcAyIKCtkJKZaJSWmZOqoYkmmA3SgiIKFjECyqGIlqRWlKAorgWTDql5KSA3AAAftSWH)

Returns: 
   KrokiEncoder object


## Methods


### krokiencoder.KrokiEncoder.dia2kroki (self,filename,dia="ditaa",ext="png")



__Args:__

* filename (string): a diagram file, for instance with the pml extension for 
                       PlantUML code, defaults to None
* dia (string): diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz', 
                  defaults to 'ditaa'
* ext (string): file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,
                  defaults to 'png'


__Returns:__

* Kroki-URL (string)

### krokiencoder.KrokiEncoder.text2kroki (self,text,dia="ditaa",ext="png")



__Args:__

* text (string): diagram text as string, for instance PlantUML 
                       code, defaults to None
* dia (string): diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz', 
                  defaults to 'ditaa'
* ext (string): file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,
                  defaults to 'png'

__Returns:__

* Kroki-URL (string)
    

### krokiencoder.KrokiEncoder.kroki2dia (self,url)



__Args:__

* url (string): a kroki URL like https://kroki.io/plantuml/svg/eNpLzkksLlZwVOBKBjOcoLQzl6OCrhaQ66Sga6fgDADcPwn7,
                       defaults to None

__Returns:__

* diagram code (string)
    
Examples:

```{.py echo=true}
import sys, os
sys.path.append(os.path.join(os.getcwd(),".."))
from KrokiEncoder import KrokiEncoder
kroki=KrokiEncoder()
text=kroki.kroki2dia('https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqOXiSgZznCAcRwVdLQUnAJ-uCKI=')
print(text)
```

### krokiencoder.KrokiEncoder.dia2file (self,diafile,dia="ditaa",ext="png",imagefile="")



__Args:__

* diafile (string): a diagram file, for instance with the pml extension for 
                       PlantUML code, defaults to None
* dia (string): diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz', 
                  defaults to 'ditaa'
* ext (string): file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,
                  defaults to 'png'
* imagefile (string): a output filename for the image file, if not given the diagram
              imagefile will have the basename of the diagram file nut with the image extension.

__Returns:__

* None
## Module Functions


## krokiencoder.main(args)


Starting the KrokiEncoder as standalone application using command line options. Can 
be directly called programatically like this:


__Args:__

* args (list): argument list in order: appname, filename, dia, ext

```
import KrokiEncoder
KrokiEncoder.main([None,'diagram.pml','plantuml','png'])
```

Here an example for converting a PlantUML file into a PNG image using the command line 
application interface:

```bash
$ KrokiEncoder.py diagram.pml plantuml png
```

Thereafter the file ```diagram.png``` should be in parallel to the file ``diagram.pml``.

here a file ``diagram.pml`` with the following content and below the output:

```{.kroki dia=plantuml,eval=false,echo=true}
@startuml
class A {
* var1
* method1()
}
class B {
* var2
* method2()
}
A -> B
@enduml
```  
## <a name="example">Examples</a>

```
kroki = KrokiEncoder()
url.ditaa = kroki$text2dia("A --> B")
url.puml  = kroki$text2dia("class Kroki { }",dia="plantml")
```  
 
## <a name="authors">AUTHOR(S)</a>

Detlef Groth, University of Potsdam, 2022-2025

## LICENSE

MIT - License
