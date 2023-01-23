---
title: Lua Filter for the document conversion using Pandoc
---

## Filter description

This folder contains a few Lua based filters for the [Pandoc](https://www.pandoc.org) based
document conversion of the Python API's.

The following filters are provided.

* `links-to-html.lua` - convert Markdown file extension's in links into HTML extension
* `filter-kroki.lua` -  convert `kroki` code blocks into diagram images
* `filter-python.lua` - execute `py` code blocks to display results of Python code evaluation

The kroki and the lua filters support the following code chunk attributes:

* filter-python.lua
    * echo - should the source code been, showm default=true
    * eval - should the Python code be evaluated, default=false

* filter-kroki.lua
    * caption - the image caption, defaults to empty string
    * dia -  diagram type should be plantuml, ditaa, graphviz or erd, defaults to "plantuml"
    * echo - should the source code been, showm default=true
    * eval - should the Python code be evaluated, default=false
    * fig_path - the image folder name if images are cached, defaults to "img"
    * fig_prefix - the image filename prefix if images are cached, defaults to "kroki"
    * title  - the image title, defaults to empty string 
    
Below a few examples (remove the space after the first backtick, required to protect the 
code against evaluation.

```
    ` ``{.kroki dia=plantuml ext=png echo=false}
    @startuml
    class A 
    class B 
    A -> B
    @enduml
    ` ``
```

This should be the output:

```{.kroki dia=plantuml ext=png echo=false}
@startuml
class A 
class B 
A -> B
@enduml
```

And now an Python code example:

``` 
    ` ``{.py eval=true}
    x = 1
    print(x)
    ` ``
```

And this should be the output (*eval=true*):
    
```{.py eval=true}
x = 1
print(x)
```

And this should be the output (*eval=false*):
    
```{.py eval=false}
x = 1
print(x)
```

And this should be the output (*eval=false echo=false*):
    
```{.py eval=false echo=false}
x = 1
print(x)
```

There is nothing ...

## Document creation

The Markdown document was converted into HTML like this:

```
pandoc README.md -o README.html --css ../docs/pydoc.css -s \
    --lua-filter filter-python.lua \
    --lua-filter filter-kroki.lua 
```

Here the resulting HTML file: [README.html](http://htmlpreview.github.io/?https://github.com/mittelmark/dbpp/blob/master/lua-filters/README.html)
