#!/usr/bin/python3

"""Read only text widget.

This is a text widget derived from the tk.Text widget where the user can't change the text.
The widget otherwise has all the methods. of the original text widget. To insert text
programmatically use the syntax `cmd('ins',index, text)`, to delete the text use the
`cmd('del',start,end)` syntax.


Examples:

```

    >>> import tkinter as tk
    >>> import dbpp.widgets.RoText as RoText
    >>> root= tk.Tk() 	
    >>> rtext = RoText.RoText(root) 
    >>> rtext.cmd("ins","end","Hello World!")
    >>> root.title('RoTtext example')
    ''
    >>> rtext.pack(fill="both",expand=True)	

```

**Author:**

- 2023 Detlef Groth

**License:**  MIT - License

"""

import os
import tkinter as tk
import tkinter.font as tkfont

class RoText(tk.Text):
    """Readonly text widget based on tkText.
    
    This is an wrapper for a read only text widget, based on the dgw::rotext widget.
    There is only one public method, `cmd` which forwards the remaining arguments
    to the original text widget. The widget methods insert and delete are doing nothing.
    To insert text you should use the `cmd` method instead.
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
        self.version = self.master.tk.call('package', 'require', 'dgw::rotext')
        tk.Widget.__init__(self, master, 'dgw::rotext', cnf, kwargs)
        self.font=tkfont.Font(family="Courier",size=12)
        self.configure(font=self.font)
        #self.bind("<Control-plus>",self._IncreaseFont)
        #self.bind("<Control-minus>",self._DecreaseFont)
    def cmd(self,cmd,*args,**kwargs):
        """Access the original methods of the tk.Text widget.
        
        This is the method to access all original methods of the tk.Text widget
        except for the `insert` and `delete` method which are disabled. 
        Instead of these methods you should use `w.cmd('ins', ...)` and 
        `w.cmd('del', ...) to insert and to delete data.
        
        Args:
            cmd (string): command of the original tk.Text widget like `configure` or `see`,
                   `insert` and `delete` are doing  nothing, use `ins` and `del` instead
            *args (list) - additional positional arguments
            **kwargs (dict) - additional key-value arguments
            
        Example:
            >>> import tkinter as tk
            >>> root= tk.Tk() 	
            >>> rtext = RoText(root) 
            >>> rtext.cmd("ins","end","Hello World!")
            >>> rtext.get("1.0","end-1c")
            'Hello World!'
            >>> rtext.pack(fill="both",expand=True)	
        """
        self.tk.call(self._w, cmd, *args,**kwargs)

if __name__ == '__main__': 	
    root= tk.Tk() 	
    import dbpp
    class TText(RoText,dbpp.widgets.TextMixins.TextFontIncreaserMixin): pass
    rtext = TText(root) 
    rtext.bindTextResize()
    rtext.cmd("ins","end","Hello World!")
    root.title('Ctext example') 
    rtext.pack(fill="both",expand=True)	
    rtext.mainloop()
