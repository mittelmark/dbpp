#!/usr/bin/env python3
"""
dbpp.kroki.KrokiEncoder - class to encode diagram code as krokio.io URL's and to decode 
  them back to text.

This class provides methods to convert diagram code for tools like 
[PlantUML](https://plantuml.com), [GraphViz](https://www.graphviz.org) or
[Ditaa](https://ditaa.sourceforge.net/) to base64 encoded URL's ready to display 
them as web images using the [https://kroki.io](https://kroki.io) and ready to edit them online
 using the [Niolesk web editor](https://niolesk.top/).

Examples:

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
"""

#' ## NAME
#'  
#' `KrokiEncoder` - class to encode diagram code as krokio.io URL's and to decode 
#'  them back to text.
#'
#' This class provides methods to convert diagram code for tools like 
#' [PlantUML](https://plantuml.com), [GraphViz](https://www.graphviz.org) or
#' [Ditaa](https://ditaa.sourceforge.net/) to base64 encoded URL's ready to display 
#' them as web images using the [https://kroki.io](https://kroki.io) and ready to edit them online
#' using the [Niolesk web editor](https://niolesk.top/).
#'  
#' Here an example with the UML diagram for the KrokiEncoder class:
#'  
#' ![ [Edit Diagram](https://niolesk.top/#https://kroki.io/plantuml/svg/eNpzKC5JLCopzc3hcs5JLC5W8C7Kz850zUvOT0ktUqjmUgABbYWUzESjtMycVA1NZJFskFqEEJhrBJRACJWkVpTAldVyOaTmpQCtAgDzkiG9) ](https://kroki.io/plantuml/svg/eNpzKC5JLCopzc3hcs5JLC5W8C7Kz850zUvOT0ktUqjmUgABbYWUzESjtMycVA1NZJFskFqEEJhrBJRACJWkVpTAldVyOaTmpQCtAgDzkiG9)
#'  
#' ## SYNOPSIS
#'
#' ```
#' from dbp.kroki.KrokiEncoder import KrokiEncoder
#' kroki = KrokiEncoder()
#' kroki.text2kroki("A --> B")
#' kroki.text2kroki("class A { }",dia='plantuml',ext='svg')  
#' kroki.dia2kroki(diafilename,dia='plantuml',ext='png')
#' ```
#'  
#' ## <a name="command">COMMAND</a>
#'
#' **KrokiEncoder()**
#'
#' > *Arguments:* None
#'
#' > *Returns:* a KrokiEncoder object
#' 

import sys, os, re
import base64 
import zlib 
import urllib.request
import requests

class KrokiEncoder:
    """
    Class to encode and decode diagram code using the 
    [https://kroki.io](https://kroki.io) web service.
    
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
        
    """
    
    # translate a diagram text file to an kroki URL
    #' **cmdName.dia2kroki(filename,dia="ditaa",ext="png")**
    #'
    #' > Encodes the given diagram file as a Kroki URL.
    #'
    #' > *Arguments:* 
    #'  
    #' > - *filename* - a diagram file for instance with Ditaa or PlantUML code
    #'   - *dia* -  the diagram type, one of the supported types for the kroki.io website such as "ditaa", "plantuml" or "graphviz", default: "ditaa"
    #'   - *ext* - the file extension for the link such as "png", "svg" or "pdf", default:"png"
    #'
    #' > *Returns:* a base64 encoded kroki URL ready to be embedded into HTML or Markdown pages.
    #'  
    
    def dia2kroki (self,filename,dia="ditaa",ext="png"):
        """
        Converts a diagram file to a Kroki URL
        
        Args:
            filename (string): a diagram file, for instance with the pml extension for 
                               PlantUML code, defaults to None
            dia (string): diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz', 
                          defaults to 'ditaa'
            ext (string): file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,
                          defaults to 'png'
        Returns:
            Kroki-URL (string)
        """
        fin = open(filename,'r')
        url = base64.urlsafe_b64encode(
            zlib.compress(fin.read().encode('utf-8'), 9)).decode('ascii')
        fin.close()
        return(f"https://kroki.io/{dia}/{ext}/{url}")
    #' **cmdName.text2kroki(text,dia="ditaa",ext="png")**
    #'
    #' > Encodes the given diagram text as a Kroki URL.
    #'
    #' > *Arguments:* 
    #'  
    #' > - *text* - diagram text as string for instance with Ditaa or PlantUML code
    #'   - *dia* -  the diagram type, one of the supported types for the kroki.io website such as "ditaa", "plantuml" or "graphviz", default: "ditaa"
    #'   - *ext* - the file extension for the link such as "png", "svg" or "pdf", default:"png"
    #'
    #' > *Returns:* a base64 encoded kroki URL ready to be embedded into HTML or Markdown pages.
    #'  
        
    def text2kroki (self,text,dia="ditaa",ext="png"):
        """
        Converts a given diagram text to a Kroki URL.
        
        Args:
            text (string): diagram text as string, for instance PlantUML 
                               code, defaults to None
            dia (string): diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz', 
                          defaults to 'ditaa'
            ext (string): file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,
                          defaults to 'png'
        Returns:
            Kroki-URL (string)
            
        """
        url = base64.urlsafe_b64encode(
            zlib.compress(text.encode('utf-8'), 9)).decode('ascii')
        return(f"https://kroki.io/{dia}/{ext}/{url}")

    #' **cmdName.kroki2dia(url)**
    #'
    #' > Decodes the given kroki URL as diagram text.
    #'
    #' > *Arguments:* 
    #'  
    #' > - *url* - a kroki URL
    #'
    #' > *Returns:* the diagram text for the given base64 encoded kroki URL.
    #'  
    
    def kroki2dia (self,url):
        """
        Converts a Kroki URL back to diagram code.
        
        Args:
            url (string): a kroki URL like https://kroki.io/plantuml/svg/eNpLzkksLlZwVOBKBjOcoLQzl6OCrhaQ66Sga6fgDADcPwn7,
                               defaults to None
        Returns:
            diagram code (string)
            
        Examples:
        
        ```{.py echo=true}
        import sys, os
        sys.path.append(os.path.join(os.getcwd(),".."))
        from KrokiEncoder import KrokiEncoder
        kroki=KrokiEncoder()
        text=kroki.kroki2dia('https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqOXiSgZznCAcRwVdLQUnAJ-uCKI=')
        print(text)
        ```
        """
        b64 = re.sub(".+/","",url)
        return(zlib.decompress(base64.urlsafe_b64decode(b64)).decode("ascii"))
        
    # download an image file
    #' **cmdName.dia2file(diafile,dia="ditaa",ext="png",imgfile="")**
    #'
    #' > Encodes the given diagram file as a Kroki URL and downloads the image belonging to this file and save it into the given image filename.
    #'
    #' > *Arguments:* 
    #'  
    #' > - *diafile* - a diagram file for instance with Ditaa or PlantUML code
    #'   - *dia* -  the diagram type, one of the supported types for the kroki.io website such as "ditaa", "plantuml" or "graphviz", default: "ditaa"
    #'   - *ext* - the file extension for the link such as "png", "svg" or "pdf", default:"png"
    #'   - *imagefile* - the image file in which to put the image data, if not given just the same basename as from the *diafile* is used
    #'
    #' > *Returns:* None
    #'  
    
    def dia2file (self,diafile,dia="ditaa",ext="png",imagefile=""):
        """
        Converts a diagram file to an image file.
        
        Args:
            diafile (string): a diagram file, for instance with the pml extension for 
                               PlantUML code, defaults to None
            dia (string): diagram type, either 'ditaa', 'plantuml', 'erd' or 'graphviz', 
                          defaults to 'ditaa'
            ext (string): file extension, either 'png', 'svg' or 'pdf', not all extensions are supported for all diagram types,
                          defaults to 'png'
            imagefile (string): a output filename for the image file, if not given the diagram
                      imagefile will have the basename of the diagram file nut with the image extension.
        Returns:
            None
        """
        url = self.dia2kroki(diafile,dia=dia,ext=ext)
        if imagefile == "":
            imagefile = re.sub("(.+)\\.[a-z0-9A-Z]+$","\\1."+ext,diafile)
        if (imagefile == diafile):
            imagefile = diafile+"."+ext
        if (os.path.exists(imagefile)):
            if os.path.getmtime(imagefile) > os.path.getmtime(diafile):
                # image file is newer than diagram file
                # no need to download it again
                return
        r = requests.get(url)
        fout = open(imagefile, 'wb')
        fout.write(r.content)
        fout.close()
    
       
def usage(args):
    '''
    Usage information for the KrokiEncoder as a standalone application."
    
    Args:  
        args (list): argument list in order: appname, filename, dia, ext
    '''
    print("Usage: {} filename dia ext".format(args[0]))
    print("     dia  is either ditaa, graphviz, erd or plantuml")
    print("     ext which url should be produced png or svg is possible")
    
def main(args):
    """
    Starting the KrokiEncoder as standalone application using command line options. Can 
    be directly called programatically like this:

    Args:  
        args (list): argument list in order: appname, filename, dia, ext
    
    ```
    import KrokiEncoder
    KrokiEncoder.main([None,'diagram.pml','plantuml','png'])
    ```
    
    Here an example for converting a PlantUML file into a PNG image using the command line 
    application interface:
    
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
    """
    kroki = KrokiEncoder()
    if not(os.path.exists(args[1])):
        print("Error: File %s does not exists!" % args[1])
        exit()
    if len(args)>2:
        if not args[2] in ['ditaa', 'erd', 'plantuml', 'graphviz']:
            print("Error: Invalid diagram type, valid types are ditaa, erd, plantuml, graphviz")
            exit()
    url=kroki.dia2kroki(args[1], dia=args[2], ext=args[3])
    kroki.dia2file(args[1],dia=args[2],ext=args[3])
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage(sys.argv)
    else:
        main(sys.argv)
        

#'  
#' ## <a name="example">Examples</a>
#'
#' ```
#'  kroki = KrokiEncoder()
#'  url.ditaa = kroki$text2dia("A --> B")
#'  url.puml  = kroki$text2dia("class Kroki { }",dia="plantml")
#' ```  
#'  
#' ## <a name="authors">AUTHOR(S)</a>
#'
#' Detlef Groth, University of Potsdam, 2022
#'
#' ## LICENSE
#'
#' MIT - License
#'  

