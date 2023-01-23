"""
Tkinter widget package developed for the course Databases and Practical Bioinformatics.

Widget package developed at the course Databases and Practical Programming
for the Master course Bioinformatics at the University of Potsdam. 

The following widgets are provided:

- [GuiBaseClass](dbpp.widgets.GuiBaseClass.md) - base class to build your own Tkinter applications
- [AutoScrollbar](dbpp.widgets.AutoScrollbar.md) - a scrollbar which autohides if not required, easier to use is the [Scrolled](Scrolled.md) method
- [Balloon](dbpp.widgets.Balloon.md) - a tooltip widgets which can use balloon popups or existing label widgets
- [Ctext](dbpp.widgets.Ctext.md) - a syntax highlighting widget based on Tcl tklib ctext widget
- [LabEntry](dbpp.widgets.LabEntry.md) - a composite widget out of ttk.Label and ttk.Entry 
- [Scrolled](dbpp.widgets.Scrolled.md) - a helper functions to attach scrollbars to widgets
- [SqlText](dbpp.widgets.SqlText.md) - a Text widget with support for SQL highlighting based on Ctext
- [StatusBar](dbpp.widgets.StatusBar.md) - a statusbar having a label for messages and a progressbar
- [TableView](dbpp.widgets.TableView.md) - a ttk.Treeview widget optimized for tabular output
- [TextMixins](dbpp.widgets.TextMixins.md) - small addons for the tk.Text widget such as font increasing shortcuts, right click popups and others
- [XTableView](dbpp.widgets.XTableView.md) - an extended version of TableView which allows easily to read in list data
- [XTreeView](dbpp.widgets.XTreeView.md) - a ttk.Treeview widget which provides icon facilities

"""
import dbpp.widgets.GuiBaseClass
import dbpp.widgets.StatusBar
import dbpp.widgets.AutoScrollbar
import dbpp.widgets.Scrolled
import dbpp.widgets.Balloon
import dbpp.widgets.LabEntry
import dbpp.widgets.TableView
import dbpp.widgets.XTableView
import dbpp.widgets.XTreeView
import dbpp.widgets.TextMixins
import dbpp.widgets.Ctext
import dbpp.widgets.SqlText

