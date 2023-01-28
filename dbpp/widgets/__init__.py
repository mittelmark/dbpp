"""
Tkinter widget package developed for the course Databases and Practical Bioinformatics.

Widget package developed at the course Databases and Practical Programming
for the Master course Bioinformatics at the University of Potsdam. 

The following widgets are provided:

- [GuiBaseClass](dbpp.widgets.guibaseclass.md) - base class to build your own Tkinter applications
- [AutoScrollbar](dbpp.widgets.AutoScrollbar.md) - ttk.Scrollbar which autohides if not required, easier to use is the [Scrolled](Scrolled.md) method
- [Balloon](dbpp.widgets.Balloon.md) - tooltip widgets which can use balloon popups or existing label widgets
- [Ctext](dbpp.widgets.Ctext.md) - syntax highlighting widget based on Tcl tklib's ctext widget
- [LabEntry](dbpp.widgets.LabEntry.md) - composite widget out of ttk.Label and ttk.Entry 
- [RoText](dbpp.widgets.RoText.md) - readonly tk.Text widget
- [Scrolled](dbpp.widgets.Scrolled.md) - helper functions to attach ttk.Scrollbar's to widgets
- [SqlText](dbpp.widgets.SqlText.md) - Text widget with support for SQL highlighting based on Ctext
- [StatusBar](dbpp.widgets.statusbar.md) - statusbar having a label for messages and a progressbar
- [TableView](dbpp.widgets.TableView.md) - ttk.Treeview widget optimized for tabular output
- [TextMixins](dbpp.widgets.TextMixins.md) - small addons for the tk.Text widget such as font increasing shortcuts, right click popups and others
- [XTableView](dbpp.widgets.XTableView.md) - extended version of TableView which allows easily to read in list data
- [XTreeView](dbpp.widgets.XTreeView.md) - ttk.Treeview widget which provides icon facilities for tree display
"""
import dbpp.widgets.guibaseclass
import dbpp.widgets.statusbar
import dbpp.widgets.autoscrollbar
import dbpp.widgets.scrolled
import dbpp.widgets.Balloon
import dbpp.widgets.LabEntry
import dbpp.widgets.TableView
import dbpp.widgets.XTableView
import dbpp.widgets.XTreeView
import dbpp.widgets.TextMixins
import dbpp.widgets.Ctext
import dbpp.widgets.SqlText
import dbpp.widgets.RoText

