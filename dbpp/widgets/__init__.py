"""
Tkinter widget package developed for the course Databases and Practical Bioinformatics.

Widget package developed at the course Databases and Practical Programming
for the Master course Bioinformatics at the University of Potsdam. 

The following widgets are provided:

- [GuiBaseClass](dbpp.widgets.guibaseclass.md) - base class to build your own Tkinter applications
- [AutoScrollbar](dbpp.widgets.autoscrollbar.md) - ttk.Scrollbar which autohides if not required, easier to use is the [Scrolled](scrolled.md) method
- [Balloon](dbpp.widgets.balloon.md) - tooltip widgets which can use balloon popups or existing label widgets
- [Ctext](dbpp.widgets.ctext.md) - syntax highlighting widget based on Tcl tklib's ctext widget
- [LabEntry](dbpp.widgets.labentry.md) - composite widget out of ttk.Label and ttk.Entry 
- [RoText](dbpp.widgets.rotext.md) - readonly tk.Text widget
- [Scrolled](dbpp.widgets.scrolled.md) - helper functions to attach ttk.Scrollbar's to widgets
- [SqlText](dbpp.widgets.sqltext.md) - Text widget with support for SQL highlighting based on Ctext
- [StatusBar](dbpp.widgets.statusbar.md) - statusbar having a label for messages and a progressbar
- [TableView](dbpp.widgets.tableview.md) - ttk.Treeview widget optimized for tabular output
- [TextMixins](dbpp.widgets.textmixins.md) - small addons for the tk.Text widget such as font increasing shortcuts, right click popups and others
- [XTableView](dbpp.widgets.xtableview.md) - extended version of TableView which allows easily to read in list data
- [XTreeView](dbpp.widgets.xtreeview.md) - ttk.Treeview widget which provides icon facilities for tree display
"""
import dbpp.widgets.guibaseclass
import dbpp.widgets.statusbar
import dbpp.widgets.autoscrollbar
import dbpp.widgets.scrolled
import dbpp.widgets.balloon
import dbpp.widgets.labentry
import dbpp.widgets.tableview
import dbpp.widgets.xtableview
import dbpp.widgets.XTreeView
import dbpp.widgets.textmixins
import dbpp.widgets.ctext
import dbpp.widgets.sqltext
import dbpp.widgets.rotext

