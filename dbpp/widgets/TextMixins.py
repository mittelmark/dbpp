#!/usr/bin/env python3
"""
The module *TextMixins* adds a few small Mixin classes for the *tk.Text* widget
to extend its functionality on the fly.

The following Mixins are currently implemented:

- TextFontIncreaserMixin - adding bindings *Ctrl-plus* and *Ctrl-minus* to change the fontsize
- TextCuaBindingsMixin  - adds a few standard bindings like *Ctrl-a* to select the text and a status aware context menu for right mouse button clicks
- TextHighLightMixin - a simple syntax highlighter for single and multiline comments as well as for keywords

Examples:

```
import tkinter as tk
from dbp.widgets.TextMixins import TextMixins
root = tk.Tk()
class text(tk.Text,TextFontIncreaserMixin,TextCuaBindingsMixin,
    TextHighLightMixin): pass
txt  = text(root,undo=True) 
txt.bindTextResize()
txt.bindCua()
txt.addHighLights(commentline="'",commentstart="/'",
    commentend="'/",keywords=[ ['@startuml','@enduml'], ['class', 'entity', 'table'] ])
txt.insert("1.0","
@startuml
'This is a comment
class A
class B
A --> B
@enduml
")
txt.updateHighLights()
txt.pack(side='top',fill='both',expand=True)
root.mainloop()        
```
"""
import re
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

# a few Mixins for tk.Text widgets

class TextFontIncreaserMixin:
    """
    Adding fontsize adjustments using Ctrl-plus, Ctrl-minus to the tk.Text widget.
    
    Mixin class for the tk.Text widget which allows to extend its functionality
    on the fly by creating an empty class like this:
    
    ```
    import tkinter as tk
    class MText(tk.Text,dbp.widgets.TextMixins.TextFontIncreaserMixin): pass
    root = tk.Tk()
    text = MText(root)
    text.bindTextResize()
    ```
    
    Now you can presse *Ctrl-Plus* to increase the font and *Ctrl-Minus* to decrease the fontsize.
    """
    def bindTextResize (self,increase="Control-plus",decrease="Control-minus",font=None):
        """
        Add the actual bindings for increasing and decreasing the fontsize using the
        *Ctrl-Plus* and *Ctrl-Minus* keys combinations.
        
        Args:
            increase (string): the key combination to increase the fontsize, defaults to "Control-plus"
            decrease (string): the key combination to decrease the fontsize, defaults to "Control-minus"            
            font (string): the prefered Font to be used, if not given searches for a platform depending good choice, defaults to None
        """
        if font is None:
            if "Monaco" in tkfont.families():
                # my favourite
                font="Monaco"
            elif "Consolas" in tkfont.families():
                # Windows Font
                font="Consolas"
            elif "Ubuntu Mono" in tkfont.families():
                # Ubuntu Font
                font="Ubuntu Mono"
            elif "SF Mono"  in tkfont.families():
                font="SF Mono"
            else:
                font="Courier"
        self.font=tkfont.Font(family=font,size=12)
        self.configure(font=self.font)
        self.bind(f"<{increase}>",self.increaseFont)
        self.bind(f"<{decrease}>",self.decreaseFont)
    def increaseFont(self,evt=None):
        """Increase the font size of the widget."""
        size = int(self.font.cget("size"))
        size += 2
        self.font.configure(size=size)
    def decreaseFont (self,evt=None):
        """Decrease the font size of the widget."""
        size = int(self.font.cget("size"))
        size -= 2
        self.font.configure(size=size)
class TextCuaBindingsMixin:
    """
    CUA bindings and right click popup menu for the tk.Text widget.
    
    Mixin class for the tk.Text widget which allows to extend its functionality
    on the fly for adding standard bindings and a Right click popup menu 
    by creating an empty class like this:
    
    Examples:
    
    ```
    import tkinter as tk
    class MText(tk.Text,dbp.widgets.TextMixins.TextCuaBindingsMixin): pass
    root = tk.Tk()
    text = MText(root)
    text.bindCua()
    ```
    
    Now you can presse *Ctrl-a* for instance to select the complete text, you get as well
    a widget status aware context menu if you press the right mouse button in the text widget.
    """

    def bindCua (self):
        """
        Adds the actual bindings Ctrl-x, Ctrl-c, Ctrl-v, Control-z, Control-a
        known as well as CUA bindings and in addition a right click context mene
        """
        #self.bind('<Control-c>', lambda evt: self.event_generate("<<Copy>>"))
        #self.bind('<Control-x>', lambda evt: self.event_generate("<<Cut>>"))
        #self.bind('<Control-v>', lambda evt: self.event_generate("<<Paste>>")) 
        #self.bind('<Control-z>', lambda evt: self.event_generate("<<Undo>>"))
        self.bind('<Control-a>', self._SelectAll)
        self.root = self.winfo_toplevel()
        if (self.root.tk.call('tk', 'windowingsystem')=='aqua'):
            self.bind('<Button-2>', self._MenuCua)
        else:
            self.bind('<Control-1>', self._MenuCua)
            self.bind("<Button-3>",  self._MenuCua)
        self.cuapop = tk.Menu(self.root,tearoff=False)
        self.cuapop.add_command(label="Undo",underline=0,accelerator="Ctrl-Z")
        self.cuapop.add_command(label="Redo",underline=0,accelerator="Ctrl-Shift-z")
        self.cuapop.add_separator()
        self.cuapop.add_command(label="Cut",underline=1,accelerator="Ctrl-X")
        self.cuapop.add_command(label="Copy",underline=0,accelerator="Ctrl-C")
        self.cuapop.add_command(label="Paste",underline=0,accelerator="Ctrl-V")
        self.cuapop.add_command(label="Delete",underline=0,accelerator="Del")        
        self.cuapop.add_separator()
        self.cuapop.add_command(label="Select All",underline=7,accelerator="Ctrl-Shift-/")        
    def _MenuCua (self,e):
        w = e.widget
        if (type(w) == str):
            w = self.root.nametowidget(w)
        for i in range(0,self.cuapop.index('end')+1):
            if (self.cuapop.type(i) == 'command'):
                self.cuapop.entryconfig(i,state="disabled")
        if  int(self.cget("undo")) == 1  and w.edit_modified() :
            self.cuapop.entryconfigure("Undo", command=lambda: w.event_generate("<<Undo>>"),state="active")
            self.cuapop.entryconfigure("Redo", command=lambda: w.event_generate("<<Redo>>"),state="active")
        if len(w.tag_ranges('sel'))>0:
            self.cuapop.entryconfigure("Cut", command=lambda: w.event_generate("<<Cut>>"),state="active")
            self.cuapop.entryconfigure("Copy", command=lambda: w.event_generate("<<Copy>>"),state="active")
            self.cuapop.entryconfigure("Delete", command=lambda: w.event_generate("<<Clear>>"),state="active")            
        cb=""
        try:
            cb=self.root.selection_get(selection="CLIPBOARD")
        except:
            cb = ""
        if cb != "":
            self.cuapop.entryconfigure("Paste",  command=lambda: w.event_generate("<<Paste>>"),state="active")
        if len(w.get('1.0','end')) > 1:
            self.cuapop.entryconfigure("Select All", command=self._SelectAll,state="active")
        self.cuapop.tk.call("tk_popup", self.cuapop, e.x_root, e.y_root)
        
    def _SelectAll(self,evt=""):
        self.tag_add('sel','1.0','end')
        # stop additional event's which might be bound to Ctrl-a 
        # like jumping cursor to the beginning of the line
        return("break")
        
class TextHighLightMixin:
    """
    Syntax highlighting for the tk.Text widget.
    
    Mixin class for the tk.Text widget which allows to extend its functionality
    on the fly for some minimal syntax highlighting by creating an empty class like this:
    
    Example:
    
    ```
    import tkinter as tk
    class MText(tk.Text,dbpp.widgets.TextMixins.TextHighLightMixin): pass
    root = tk.Tk()
    text = MText(root)
    text.addHighLights(linecomment="^\s*'",keywords=[ 
        ['@startuml','@enduml', '@startmindmap','@endmindmap'], 
        ['class', 'entity', 'table'] ])
    ```
    
    """

    def addHighLights(self,commentline="^\s*#",commentstart=None,commentend=None,keywords=list(),strings=True):
        """
        Adds the actual syntax highlighting and the binding for updates of the high lighting after pressing Up, Down or Return.
        For updating after a new file is loaded see updateHighLights
        
        Args:
            commentline  (regex): the regular expression to start a single line comment, defaults to "^\s*#"
            commentstart (regex): the regular expression to start a multi line comment, defaults to None
            commentend   (regex): the regular expression to start a multie line comment, defaults to None            
            keywords (list): nested list of keywords, each sublist will be given a different color, defaults to list()
            strings (bool): should strings be highlighted, defaults to True
            
        """
        self.bind("<KeyPress>",self._KeyPressHighLights)
        self.bind("<<Redo>>",self._HighLightRedo)
        self.bind("<<Undo>>",self._HighLightUndo)
        self.bind("<<Cut>>",self._HighLightCut)
        self.bind("<<Copy>>",self._HighLightCopy)
        self.bind("<<Paste>>",self._HighLightPaste)
        self.tag_config("comment", foreground="#339966")
        if commentstart is None:
            commentstart = ""
        if commentend is None:
            commentend = ""    
        self.commentline  = commentline
        self.commentstart = commentstart
        self.commentend   = commentend
        self.HighlightList = keywords
        self.strings = strings
        self.tag_configure("orange", foreground = "orange")
        self.tag_configure("blue", foreground = "blue")
        self.tag_configure("purple", foreground = "purple")
        self.tag_configure("green", foreground = "green")
        self.tag_configure("red", foreground = "darkred")
        self.tag_configure("string", foreground = "tomato")        
        self.tags = ["orange", "blue", "purple", "green", "red"]
    def updateHighLights (self):
        """
        Updates the current given syntax highlights for instance after
        loading a new file into the widget. If this file should support other
        highlighting you should before again call the method addHighLights.
        """       
        comment = False
        string = False
        self.tag_remove("comment","1.0","end")
        self.tag_remove("orange","1.0","end")
        self.tag_remove("blue","1.0","end")
        self.tag_remove("purple","1.0","end")        
        self.tag_remove("green","1.0","end")        
        self.tag_remove("red","1.0","end")        
        self.tag_remove("string","1.0","end")                
                        
        for i in range(1,int(re.sub("^([0-9]+)\..+","\\1",self.index('end') ))):
            start=""+str(i)+".0"
            end=""+str(i)+".end"
            if (self.commentline != ""):
                if (re.search(self.commentline,self.get(start,end))):
                    self.tag_add("comment",start,end)
                    continue
            if (self.commentstart != ""):
                if (comment and re.search(self.commentend,self.get(start,end))): 
                    self.tag_add("comment",startindex,end)
                    comment = False
                    continue
                elif (re.search(self.commentstart,self.get(start,end))):
                    comment = True
                    startindex = start
            if not(comment):
                if (self.strings):
                    for m in re.finditer("[\"'](.+?)[\"']", self.get(start,end)):
                        for [x,y] in [(m.start(0), m.end(0))]: 
                            self.tag_add("string",str(i)+"."+str(x),str(i)+"."+str(y))
                
        self._HighlightKeywords()
    def _HighlightKeywords (self):
        # code adapted from https://coderslegacy.com/python-gui-projects-with-tkinter-code/
        start = "1.0"
        end   = "end"
        for mlist in self.HighlightList:
            idx = int(self.HighlightList.index(mlist))
            for word in mlist:
                self.mark_set("matchStart", start)
                self.mark_set("matchEnd", start)
                self.mark_set("SearchLimit", end)
                mycount = tk.IntVar()
                while True:
                    index = self.search(word,"matchEnd","SearchLimit", count=mycount, regexp = False)
                    if index == "": break
                    if mycount.get() == 0: break
                    self.mark_set("matchStart", index)
                    self.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
                    preIndex = "%s-%sc" % (index, 1)
                    postIndex = "%s+%sc" % (index, mycount.get())
                    if (len(self.tag_names(index)) != 0): continue
                    if self._CheckWord(index, preIndex, postIndex):
                        self.tag_add(self.tags[idx], "matchStart", "matchEnd")   
    def _CheckWord (self, index, pre, post):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","_"]
        if self.get(pre) == self.get(index):
            pre = index
        else:
            if self.get(pre) in letters:
                return 0
            if self.get(post) in letters:
                return 0
        return 1                    
    def _HighLightRedo (self,evt=None):
        self.edit_redo()
        self.updateHighLights()
        return("break")
    def _HighLightUndo (self,evt=None):
        self.edit_undo()
        self.updateHighLights()
        return("break")
    def _HighLightCopy (self,evt=None):
        self.tk.call('tk_textCopy', self)
        self.updateHighLights()
        return("break")
    def _HighLightCut (self,evt=None):
        self.tk.call('tk_textCut', self)
        self.updateHighLights()
        return("break")
    def _HighLightPaste (self,evt=None):
        self.tk.call('tk_textPaste', self)
        self.updateHighLights()
        return("break")
    def _KeyPressHighLights(self,evt):
        #if (evt.keysym == "space"):
        if (evt.keysym in ["Return","Up","Down"]): 
            self.updateHighLights()        

if __name__ == "__main__":
    root = tk.Tk()
    class text(tk.Text,TextFontIncreaserMixin,TextCuaBindingsMixin,TextHighLightMixin): pass
    txt  = text(root,undo=True) 
    txt.bindTextResize()
    txt.bindCua()
    txt.addHighLights(commentline="'",commentstart="/'",commentend="'/",keywords=[ 
                ['@startuml','@enduml','@startditaa','@enddita','@startmindmap','@endmindmap'], 
                ['class','abstract','annotation','interface','class', 'object','entity', 'table','node','package','namespace','extends','implements'],
                ['hide', 'show','remove'],
                ['skinparam','style','scale','header', 'footer', 'title','note', 'end note'],
                ['!define','!theme','!function', '!endfunction','!return','!procedure','!endprocedure','!include','!includesub'] ])
    txt.insert("1.0","@startuml\n'This is a comment\nclass A\nclass B\nA --> B\n@enduml\n")
    txt.updateHighLights()
    txt.pack(side='top',fill='both',expand=True)
    root.mainloop()        
