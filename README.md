# README

Repository for the course Databases and Practical Programming at the University of Potsdam

The following applications will be added:

* mkdoc - create API documentation from Markdown
* kroki - encode diagram code as kroki URL's (done)
* [sfa](dbpp/sfa/__main__.py)   - create single file applications from a few Python source code files
* SQLViewer - an SQLViewer application forSQLite databases
* [PumlEditor](docs/dbpp.peditor.PumlEditor.md) - an Diagram Editor with preview functionality started with `python -m dbpp.peditor (diagramfile)` (done)

![PumlEditor](docs/peditor.png)

The following libaries will be as well added:

* [dbpp.widgets](docs/dbpp.widgets.md) - collection of Tkinter-widgets to build applications (done)
* [dbpp.kroki.Encoder](dbpp.kroki.KrokiEncoder) - class [KrokiEncoder](https://github.com/mittelmark/dbpp/blob/main/dbpp/kroki/KrokiEncoder.py)
- [dbpp.utils.SqlUtils](docs/dbpp.utils.SqlUtils.md) - class with utility functions for Python databases.

## Installation

You can install this package using the following command:

```
$ pip3 install git+https://github.com/mittelmark/dbpp.git --user
$ # after successfull install try this
$ python3 -m dbpp.kroki
$ # which should give yo a message like 
$ I am kroki __main__.py
$ python3 -m dbpp.peditor   # should start the PumlEditor
$ python3 -m dbpp.sfa  -h   # should display help for the single file application packer
```

## dbpp.widgets

A Python package with the following Tkinter widgets 
([HTML documentation](http://htmlpreview.github.io/?https://github.com/mittelmark/dbpp/blob/master/docs/dbpp.widgets.html)):

- [GuiBaseClass](docs/dbpp.widgets.guibaseclass.md) - base class to build your own Tkinter applications
- [AutoScrollbar](docs/dbpp.widgets.autoscrollbar.md) - a scrollbar which autohides if not required, easier to use is the [Scrolled](dbpp.widgets.scrolled.md) method
- [Balloon](docs/dbpp.widgets.balloon.md) - a tooltip widgets which can use balloon popups or existing label widgets
- [Ctext](docs/dbpp.widgets.ctext.md) - a syntax highlighting widget based on Tcl tklib ctext widget
- [LabEntry](docs/dbpp.widgets.labentry.md) - a composite widget out of ttk.Label and ttk.Entry 
- [RoText](docs/dbpp.widgets.rotext.md) - read only tk.Text widget based on a Tcl widget created with Tcl's snit library
- [Scrolled](docs/dbpp.widgets.scrolled.md) - a helper functions to attach scrollbars to widgets
- [SqlText](docs/dbpp.widgets.sqltext.md) - a Text widget with support for SQL highlighting based on Ctext
- [StatusBar](docs/dbpp.widgets.statusbar.md) - a statusbar having a label for messages and a progressbar
- [TableView](docs/dbpp.widgets.tableview.md) - a ttk.Treeview widget optimized for tabular output
- [TextMixins](docs/dbpp.widgets.textmixins.md) - small addons for the tk.Text widget such as font increasing shortcuts, right click popups and others
- [XTableView](docs/dbpp.widgets.xtableview.md) - an extended version of TableView which allows easily to read in list data
- [XTreeView](docs/dbpp.widgets.xtreeview.md) - a ttk.Treeview widget which provides icon facilities

## Other packages
 

- [dbpp.kroki.KrokiEncoder](docs/dbpp.kroki.krokiencoder.md) - class with functions to encode and decode diagrams as Kroki URL's
- [dbpp.utils.SqlUtils](docs/dbpp.utils.sqlutils.md) - class with utility functions for Python databases.

## Applications

### sfa - Single File Application Packer

Command  line tool to combine a few Python files into a single  Python file if
these files follow the application  layout used in the course  "Introduction to
Databases and Practical Programming" at the University of Potsdam, Germany.

Here an example to combine  file1.py and file2.py into an  application  app.py
and then install this as an application into the users bin folder:

```bash
python3 -m dbpp.sfa file1.py file2.py -o app.py
chmod 755 app.py
mv app.py ~/bin
app.py -h
``` 

### kroki - Kroki Diagram Encoder

This a command line tool to encode diagram code such as [GraphViz](https://www.graphviz.org) (.dot), [PlantUML](https://www.plantuml.com) (.pml) or [Ditaa](https://github.com/stathissideris/ditaa) (.dit) files as image url's using the [kroki](https://kroki.io) webservice or backtranslates image url's into diagram code.

Here an example for a backtranslation of an url into diagram code:

```
$ python3 -m dbpp.kroki https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA==
class A { }
```

### peditor - the PumlEditor

This a graphical application to editdiagram code such as [GraphViz](https://www.graphviz.org) (.dot), [PlantUML](https://www.plantuml.com) (.pml) or [Ditaa](https://github.com/stathissideris/ditaa) (.dit) files
and preview the image right of the editor window. This tool is as well using the [kroki](https://kroki.io) webservice to translate the diagram code
into an image which is downloaded in parallel to the diagram file.

Here is shown how you can execute the program if the package is installed.

```
$ python3 -m dbpp.peditor ?diagramfile? &
```
