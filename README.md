# README

Repository for the course Databases and Practical Programming at the University of Potsdam

The following applications will be added:

* mkdoc - create API documentation from Markdown
* kroki - encode diagram code as kroki URL's (done)
* sfa   - create single file applications from a few Python source code files
* SQLViewer - an SQLViewer application forSQLite databases
* PumlEditor - an Diagram Editor with preview functionality

The following libaries will be as well added:

* dbpp.widgets - collection of Tkinter-widgets to build applications
* kroki - a class [KrokiEncoder](https://github.com/mittelmark/dbpp/blob/main/dbpp/kroki/KrokiEncoder.py)

# Installation

You can install this package using the following command:

```
$ pip3 install git+https://github.com/mittelmark/dbpp.git --user
$ # after successfull install try this
$ python3 -m dbpp.kroki
$ # which should give yo a message like 
$ I am kroki __main__.py
```

# Running the application

## kroki

This a command line tool to encode diagram code such as [GraphViz](https://www.graphviz.org) (.dot), [PlantUM](https://www.plantuml.org) (.pml) or [Ditaa](https://github.com/stathissideris/ditaa) (.dit) files as image url's using the [kroki](https://kroki.io) webservice or backtranslates image url's into diagram code.

Here an example for a backtranslation of an url into diagram code:

```
$ python -m dbpp kroki https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA==
class A { }
```
