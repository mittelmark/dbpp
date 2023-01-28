#!/usr/bin/python3

# ctext.py - Copyright (c) 2017 Pat Thoyts <patthoyts@users.sourceforge.net>
#
# SPDX-License-Identifier: BSD-3-Clause
# 2020 small modifications to use internal tcllibs directory by Detlef Groth, 2020


"""Python wrapper for the Tklib ctext widget.

This is a text widget derived from the tk.Text widget with support for syntax highlighting and line numbers.

See the Tk documentation for complete details of the use of this widget
[here](https://core.tcl-lang.org/tklib/doc/trunk/embedded/md/tklib/files/modules/ctext/ctext.md).

Examples:

```
import tkinter as tk
import dbpp.widget.ctext as Ctext
root= tk.Tk() 	
ctext = Ctext(root) 
ctext.add_highlight_class('DML1', 'blue', ['select','SELECT','from','FROM'])
ctext.add_highlight_class('DML2', 'blue', ['and', 'AND', 'as','AS', 'or', 'OR'])
ctext.add_highlight_class('functions','OrangeRed3',  ['avg', 'AVG', 'count','COUNT']), 		
ctext.add_highlight_chars('math operators', 'magenta',  ['*','>','<','='])    	
ctext.add_highlight_regexp("comment","dark green", "--.+")
ctext.add_highlight_regexp("string","magenta", "['\"].+?['\"]")
ctext.enable_c_comments(True)

ctext.tag_configure('_cComment',foreground="dark green")
root.title('Ctext example') 
ctext.pack()	
ctext.insert("end", "select * from sample where id == '1' or id == \"Hello\"\n-- a comment\n new statement\n/*\nc-style comment passing\n multiple lines\n*/")
ctext.highlight('1.0','end')
ctext.mainloop()
```

**Authors:**

- 2017 Pat Thoyts
- 2020-2023 Detlef Groth

**License:**  MIT - License

"""

import os
import tkinter as tk
import tkinter.font as tkfont

class Ctext(tk.Text):
    """Python wrapper for the Tklib ctext widget
    
    Attributes:
        highlight (bool): Takes a boolean value which defines whether or not to highlight text which is inserted or deleted. The default is True
        linemap (bool): line numbers left of the text widget, defaults to True
        linemapbg (string): background color of the linemap, default is like in the text widget
        linemapfg (string): foreground color of the linemap, default is like in the text widget
        linemap_select_fg (string): Changes the selected line foreground. The default is black.
        linemap_select_bg (string): Changes the selected line background. The default is yellow.
        linemap_mark_command (string): Calls a procedure or command with the pathName of the ctext window, the type which is either marked or unmarked, and finally the line number selected. The proc prototype is: `linemark_cmd (win, type, line)
        linemap_markable (bool): Takes a boolean value which specifies whether or not lines in the linemap are markable with the mouse. The default is True.
    """
    def __init__(self, master=None, cnf={}, **kwargs):
        """Initialize the ctext wrapper.
        
        Args:
            master (ttk.Frame): the parent widget, usually a ttk.Frame, if not given the toplevel is choosen, default: None
            cnf, **kwargs (dict): options delegated to the ctext widget
             
        """
        if master:
            self.master = master
        else:
            self.master = tk._default_root
        self.master.tk.call("lappend", "auto_path",os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','tcllibs'))
        self.version = self.master.tk.call('package', 'require', 'ctext')
        tk.Widget.__init__(self, master, 'ctext', cnf, kwargs)
        self.font=tkfont.Font(family="Courier",size=12)
        self.configure(font=self.font)
        self.bind("<Control-plus>",self._IncreaseFont)
        self.bind("<Control-minus>",self._DecreaseFont)
    # public functions
    def highlight(self, start_index, end_index):
        """Highlight the text between start_index and end_index."""
        self.tk.call(self._w, 'highlight', start_index, end_index)

    def fastdelete(self, index, index2=None):
        """Delete the text range specified without updating the highlighting.
        Arguments are identical to the delete method."""
        self.tk.call(self._w, 'fastdelete', index, index2)

    def fastinsert(self, index, *args):
        """Insert text without updating the highlighting.
        Arguments are identical to the insert method."""
        self.tk.call(self._w, 'fastinsert', index, *args)

    def copy(self):
        """Copy the selected text from this widget to the clipboard."""
        self.tk.call('tk_textCopy', self._w)

    def cut(self):
        """Copy the selected text from this widget to the clipboard and then delete it from the widget."""
        self.tk.call('tk_textCut', self._w)

    def paste(self):
        """Paste the contents of the clipboard to the insertion point of the ctext widget."""
        self.tk.call('tk_textPaste', self._w)

    def append(self):
        """Append the selected text from this widget to the clipboard."""
        self.tk.call(self._w, 'append')

    def add_highlight_class(self, classname, color, wordlist):
        """Add a highlighting class `classname` to the widget using the given color
        containing all the words in the `wordlist`.
        
        Args:
            classname (string): a classname used as text tag internally
            color (string): a color used for highlighting
            wordlist (string): a list of keywords, case sensitive
        """
        self.tk.call('ctext::addHighlightClass', self._w, classname, color, wordlist)

    def add_highlight_prefix(self, classname, color, char):
        """Add a highlighting class that matches any word that starts with the specified `char`.
        
        Args: 
            classname (string): a classname used as text tag internally
            color (string): a color used for highlighting
            char (chr): a single character for highlighting text which comes after that char
        """
        self.tk.call('ctext::addHighlightClassWithOnlyCharStart', self._w, classname, color, char)

    def add_highlight_chars(self, classname, color, chars):
        """Add a highlighting class that matches any of the characters contained in `chars`.
        
        Args: 
            classname (string): a classname used as text tag internally
            color (string): a color used for highlighting
            chars (list): list of single characters for highlighting text which comes after that char
        """
        self.tk.call('ctext::addHighlightClassForSpecialChars', self._w, classname, color, chars)

    def add_highlight_regexp(self, classname, color, pattern):
        """Add a highlighting class that matches a regular expression to apply the chosen color.
        Args: 
            classname (string): a classname used as text tag internally
            color (string): a color used for highlighting
            pattern (regex): a regular expression used for for highlighting text
        """
        self.tk.call('ctext::addHighlightClassForRegexp', self._w, classname, color, pattern)

    def clear_highlight_classes(self):
        """Remove all highlight classes from this widget."""
        self.tk.call('ctext::clearHighlightClasses', self._w)

    def get_highlight_classes(self):
        """Return a list of all the highlight class names defined for this widget."""
        return self.tk.call('ctext::getHighlightClasses', self._w)

    def delete_highlight_class(self, classname):
        """Delete the selected highlight class from the widget."""
        self.tk.call('ctext::deleteHighlightClass', self._w, classname)

    def enable_c_comments(self, enable):
        """Enable C comment highlighting.
        
        The class for c-style comments is `_cComment`. This highlighting is disabled by default.
        
        Args:
            enable (bool): if True C comments are enabled
        """
        if enable:
            cmd = 'ctext::enableComments'
        else:
            cmd = 'ctext::disableComments'
        self.tk.call(cmd, self._w)
    # private functions
    def _IncreaseFont (self,evt):
        size = int(self.font.cget("size"))
        size += 2
        self.font.configure(size=size)
    def _DecreaseFont (self,evt):
        size = int(self.font.cget("size"))
        size -= 2
        self.font.configure(size=size)


if __name__ == '__main__': 	
    root= tk.Tk() 	
    ctext = Ctext(root) 
    ctext.add_highlight_class('DML1', 'blue', ['select','SELECT','from','FROM'])
    ctext.add_highlight_class('DML2', 'blue', ['and', 'AND', 'as','AS', 'asc', 'ASC', 
    		'between','BETWEEN', 'by', 'BY', 'desc','DESC', 'distinct', 'DISTINCT', 'group','GROUP', 		'having', 'HAVING','in','IN','inner', 'INNER', 'join', 'JOIN', 'left', 'LEFT', 'like','LIKE', 		'limit','LIMIT', 'max','MAX','min','MIN', 'or', 'OR', 'order',  'ORDER', 'outer', 'OUTER', 		'right', 'RIGHT', 'round', 'ROUND','where','WHERE', ])
    ctext.add_highlight_class('functions','OrangeRed3', ['avg', 'AVG', 'count','COUNT', 		
        'except','EXCEPT', 'intersect','INTERSECT', 'sum', 'SUM', 'union','UNION'])
    ctext.add_highlight_chars('math operators', 'magenta', ['*','>','<','='])    	
    ctext.add_highlight_regexp("comment","dark green", "--.+")
    ctext.add_highlight_regexp("string","magenta", "['\"].+?['\"]")
    ctext.enable_c_comments(True)

    ctext.tag_configure('_cComment',foreground="dark green")
    print(ctext.tag_names())
    root.title('Ctext example') 
    ctext.pack()	
    ctext.insert("end", "select * from sample where id == '1' or id == \"Hello\"\n-- a comment\n new statement\n/*\nc-style comment passing\n multiple lines\n*/")
    ctext.highlight('1.0','end')
    ctext.mainloop()
