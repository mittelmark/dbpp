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

[dbpp.kroki](dbpp.kroki.md) - 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md) -
[dbpp.utils](dbpp.utils.md) - 
[dbpp.utils.SqlUtils](dbpp.utils.SqlUtils.md)  -

**apps:** [dbpp.peditor](dbpp.peditor.PumlEditor.md)


</center>

<!-- markdownlint-disable -->

<a href="../dbpp/kroki/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `kroki`
KrokiEncoder class and kroki command line application. 

For the KrokiEncoder class look at the class documentation  [dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md).  Here nun first follows the application help for the command line application. 

You can run the application in two ways either you translate  a kroki URL into diagram code or you encode a diagram into an URL. 

Here is how to decode an image URL into diagram text: 

```
$ python3 -m dbpp.kroki https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA==
class A { }
``` 

And here it is shown how to encode an existing diagram file  to an URL: 

```
$ cat test2.dot
digraph g {
     node[shape=box,color=skyblue,style=filled];
     { rank=same; A; B; C; }
     A -> B -> C;
}
$ python3 dbpp.kroki test2.dot
https://kroki.io/graphviz/png/eNodik0OQDAUBvc9xXcATvBSCY4hFqWPNh6VloSIu_uZxWxmrB-jWR1GXAovS7DcJGdW1l04sj5IiDpNZyc7Z2k7hfXgRdi29P8XolkmnczMhJJQEWrC_bcSeYHqU03qVuoBopMgLA==
``` 

Here is the image: 

![](https://kroki.io/graphviz/png/eNodik0OQDAUBvc9xXcATvBSCY4hFqWPNh6VloSIu_uZxWxmrB-jWR1GXAovS7DcJGdW1l04sj5IiDpNZyc7Z2k7hfXgRdi29P8XolkmnczMhJJQEWrC_bcSeYHqU03qVuoBopMgLA==) 

If you like to change the image format to svg, just replace the png term with svg in the URL. 

**Global Variables**
---------------
- **KrokiEncoder**




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
