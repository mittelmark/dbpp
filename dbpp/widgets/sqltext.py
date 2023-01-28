#!/usr/bin/python3
"""
SQL syntax aware text widdget with syntax highlighting

This is a [Ctext](Ctext.html) based Text widget which supports SQL
syntax for highlighting SQL code.

Examples:

```
import tkinter as tk
from dbpp.widgets.sqltext import SqlText
root= tk.Tk() 	
ctext = SqlText(root,background='gray90',border=5,relief='flat') 
root.title('SqlText example') 
ctext.pack(side='top',fill='both',expand=True)	
ctext.insert("end", "select * from sample where id == '1' or id == 'Hello'\n-- a comment\n new statement\n/*\nc-style comment passing\n multiple lines\n*/")
ctext.highlight('1.0','end')

# just sample execution on ctrl-enter
def bindExample(evt=None,widget=None):
    print(widget.get('1.0','end'))
    return("break")

ctext.bind('<Control-Return>',lambda evt: bindExample(widget=ctext))

root.mainloop()
```

"""

import os
import tkinter as tk
import tkinter.font as tkfont
import dbpp.widgets.ctext as Ctext

class SqlText(Ctext.Ctext):
    """Python wrapper for the Tklib ctext widget which supports SQL highlighting.
    
    All options and methods of the Ctext widget and the tk.Text widget are supported.
    """
    def __init__(self, master=None, cnf={}, **kwargs):
        """Initialize the wrapper widget.
        
        Args:
            master (ttk.Frame): the parent widget, usually a ttk.Frame, if not given the toplevel is choosen, default: None
            cnf, **kwargs (dict): options delegated to the Ctext and tk.Text widget
        """
        if master:
            self.master = master
        else:
            self.master = tk._default_root
        self.master.tk.call("lappend", "auto_path",os.path.join(os.path.dirname(os.path.abspath(__file__)),'tcllibs'))
        self.version = self.master.tk.call('package', 'require', 'ctext')
        tk.Widget.__init__(self, master, 'ctext', cnf, kwargs)
        self.add_highlight_class('DML1', 'blue', ['select','SELECT','from','FROM'])
        self.add_highlight_class('DML2', 'blue', ['and', 'AND', 'as','AS', 'asc', 'ASC', 
    		'between','BETWEEN', 'by', 'BY', 'desc','DESC', 'distinct', 'DISTINCT', 'group','GROUP', 		'having', 'HAVING','in','IN','inner', 'INNER', 'join', 'JOIN', 'left', 'LEFT', 'like','LIKE', 		'limit','LIMIT', 'max','MAX','min','MIN', 'or', 'OR', 'order',  'ORDER', 'outer', 'OUTER', 		'right', 'RIGHT', 'round', 'ROUND','where','WHERE', ])
        self.add_highlight_class('functions','OrangeRed3', ['avg', 'AVG', 'count','COUNT', 		
            'except','EXCEPT', 'intersect','INTERSECT', 'sum', 'SUM', 'union','UNION'])
        self.add_highlight_chars('math operators', 'magenta', ['*','>','<','='])    	
        self.add_highlight_regexp("comment","dark green", "--.+")
        self.add_highlight_regexp("string","magenta", "['\"].+?['\"]")
        self.enable_c_comments(True)
        self.tag_configure('_cComment',foreground="dark green")
        # don't know why inheritance for the binding does not work
        # so we repeat the lines from Ctext here ...
        self.font=tkfont.Font(family="Courier",size=12)
        self.configure(font=self.font)
        self.bind("<Control-plus>",self._IncreaseFont)
        self.bind("<Control-minus>",self._DecreaseFont)


if __name__ == '__main__': 	
    root= tk.Tk() 	
    ctext = SqlText(root,background='gray90',border=5,relief='flat') 
    root.title('SqlText example') 
    ctext.pack(side='top',fill='both',expand=True)	
    ctext.insert("end", "select * from sample where id == '1' or id == \"Hello\"\n-- a comment\n new statement\n/*\nc-style comment passing\n multiple lines\n*/")
    ctext.highlight('1.0','end')
    # just sample execution on ctrl-enter
    def bindExample(evt=None,widget=None):
        print(widget.get('1.0','end'))
        return("break")

    ctext.bind('<Control-Return>',lambda evt: bindExample(widget=ctext))

    root.mainloop()


