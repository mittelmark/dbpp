"""
KrokiEncoder class and kroki command line application.

For the KrokiEncoder class look at the class documentation 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md). 
Here nun first follows the application help for the command
line application.

You can run the application in two ways either you translate 
a kroki URL into diagram code or you encode a diagram into
an URL.

Here is how to decode an image URL into diagram text:

```
$ python3 -m dbpp.kroki https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA==
class A { }
```

And here it is shown how to encode an existing diagram file 
to an URL:

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
"""

from . import krokiencoder
