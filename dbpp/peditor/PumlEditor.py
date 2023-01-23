#!/usr/bin/env python3
"""
Example GUI application to create diagram using the https://kroki.io webservice.

This is an example GUI class to demostrate the following principles of
object oriented programming:

- inheritance - inheriting from GuiBaseClass
- composition - embedding KrokiEncoder
- mixins - including TextMixins for the tk.Text widget

You should be able to run this application from the terminal direct if the dbpp package is installed completly using this syntax:

    python -m dbpp.peditor ?DIAGRAMFILE?
    
The filename for a diagram is optional.

Here an image of the application:
 
![](peditor.png)
"""

import os, sys, re
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
import tkinter.filedialog as filedialog
from dbpp.widgets.GuiBaseClass import GuiBaseClass
from dbpp.kroki.KrokiEncoder import KrokiEncoder
from dbpp.widgets.Scrolled import Scrolled
import dbpp.widgets.TextMixins as TextMixins
# create a Mixin class 
class text(tk.Text,TextMixins.TextFontIncreaserMixin,TextMixins.TextCuaBindingsMixin,TextMixins.TextHighLightMixin): pass
class PumlEditor(GuiBaseClass):
    def __init__(self,root):
        super().__init__(root)
        # use getMenu to get file menu (mnu)
        # use mnu.insert_command(index,options) for 
        # insering new menues at a certain index
        # before File->Exit for instance
        mnu_file=self.getMenu('File')      
        mnu_file.insert_command(0,label="New ...",underline=0,command=self.fileNew, accelerator="Ctrl-n")
        mnu_file.insert_command(1,label="Open ...",underline=0,command=self.fileOpen, accelerator="Ctrl-o")
        mnu_file.insert_command(2,label="Save ...",underline=0,command=self.fileSave, accelerator="Ctrl-s")        
        mnu_file.insert_command(3,label="Save As ...",underline=1,command=self.fileSaveAs,accelerator="Ctrl-Shift-s")
        mnu_file.insert_command(4, label="Insert ...", command=self.fileInsert, underline=0)
        self.root.bind("<Control-n>", self.fileNew)
        self.root.bind("<Control-o>", self.fileOpen)
        self.root.bind("<Control-s>", self.fileSave)
        self.root.bind("<Control-S>", self.fileSaveAs)
        self.addEditMenu(target=None)
        mnu_url=self.getMenu('URL',underline=0)
        mnu_url.insert_command(0,label="Convert Text to URL",underline=8,command=self.text2url)
        mnu_url.insert_command(1,label="Convert URL to Text",underline=8,command=self.url2text)        
        mnu_tpl=self.getMenu('Templates',underline=0)
        mnu_tpl.insert_command(0,label="Class Diagram",underline=0,command=self.templateClass)
        mnu_tpl.insert_command(1,label="Database",underline=0,command=self.templateDatabase)        
        mnu_tpl.insert_command(2,label="Ditaa",underline=1,command=self.templateDitaa)
        mnu_tpl.insert_command(3,label="Mindmap",underline=0,command=self.templateMindmap)        
        mnu_tpl.insert_separator(4)
        mnu_tpl.insert_command(5,label="List colors",underline=6,command=lambda: self.templateLists("colors"))        
        mnu_tpl.insert_command(6,label="List fonts",underline=6,command=lambda: self.templateLists("listfonts"))
        mnu_tpl.insert_command(7,label="List icons",underline=8,command=lambda: self.templateLists("listopeniconic","https://plantuml.com/openiconic"))        
        mnu_tpl.insert_command(8,label="List sprites",underline=6,command=lambda: self.templateLists("listsprites","https://plantuml.com/sprite")) 
        mnu_tpl.insert_command(9,label="List libraries",underline=8,command=lambda: self.templateLists("stdlib","https://plantuml.com/stdlib"))
        mnu_tpl.insert_command(10,label="List version",underline=6,command=lambda: self.templateLists("version","https://plantuml.com/faq"))        
        mnu_tpl.insert_command(11,label="List license",underline=9,command=lambda: self.templateLists("license","https://plantuml.com/faq"))                
        mnu_opt=self.getMenu('Options',underline=0)
        mnu_opt.insert_command(0,label="Font increase",underline=5,command=lambda: self.text.increaseFont(), accelerator="Ctrl-Plus")
        mnu_opt.insert_command(1,label="Font decrease",underline=5,command=lambda: self.text.decreaseFont(),accelerator="Ctrl-Minus")        
        # insert new menu points
        frame=self.getFrame()
        # insert tk.Text now in a PanedWindow
        self.pw = ttk.PanedWindow(frame,orient="horizontal")
        self.tframe = ttk.Frame(self.pw)
        self.text = text(self.tframe,wrap='word',undo=True,border=6,relief="flat")
        self.text.bindTextResize()

        self.text.bindCua()
        self.setEditTarget(self.text)
        #self.text.bind("<<Redo>>",lambda evt: self.text.updateHighLights())
        self.text.addHighLights(commentline="'",commentstart="/'",
            commentend="'/",keywords=[ 
                ['@startuml','@enduml','@startditaa','@enddita','@startmindmap','@endmindmap'], 
                ['abstract','annotation','interface','class', 'object','entity', 'table','node','package','namespace','extends','implements'],
                ['hide', 'show','remove'],
                ['skinparam','style','scale','header', 'footer', 'title','note', 'end note'],
                ['!define','!theme','!function', '!endfunction','!return','!procedure','!endprocedure','!include','!includesub'] ])
        Scrolled(self.text)
        self.text.insert('end',"Hello start writing, please ...")  
        self.text.delete('1.0','end')      
        
        self.pw.add(self.tframe)
        # now the image widget
        self.imagewidget = ttk.Label(self.pw,text="Image Widget",anchor="center")
        self.pw.add(self.imagewidget)
        self.filename    = ""
        self.insertfile  = ""
        self.lastfiledir = os.getcwd()
        self.addStatusBar()
        self.message("Hello I am Puml!!")
        self.filetypes=(
            ('Puml files', '*.pml'),
            ('Ditaa files', '*.dit'),            
            ('Erd files', '*.erd'),
            ('Graphviz files', '*.dot'),
            ('Text files', '*.txt'),
            ('All Files', '*.*'))
        self.pw.pack(side="top",fill="both",expand=True)
        self.kroki = KrokiEncoder()
        imgdata="""
           R0lGODlhEAAQAIMAAPwCBAQCBPz+/ISChKSipMTCxLS2tLy+vMzOzMTGxNTS
           1AAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAQABAAAARlEMgJQqDYyiDG
           rR8oWJxnCcQXDMU4GEYqFN4UEHB+FEhtv7EBIYEohkjBkwJBqggEMB+ncHha
           BsDUZmbAXq67EecQ02x2CMWzkAs504gCO3qcDZjkl11FMJVIN0cqHSpuGYYS
           fhEAIf5oQ3JlYXRlZCBieSBCTVBUb0dJRiBQcm8gdmVyc2lvbiAyLjUNCqkg
           RGV2ZWxDb3IgMTk5NywxOTk4LiBBbGwgcmlnaHRzIHJlc2VydmVkLg0KaHR0
           cDovL3d3dy5kZXZlbGNvci5jb20AOw==
        """
        self.image = tk.PhotoImage(data=imgdata)
        self.imagewidget.configure(image=self.image)
        self.text.edit_modified(False)
        # Have fun!
    def fileNew (self,evt=None):
        if (self.text.edit_modified()):
            answer = mbox.askyesnocancel('Question ...', 'Text was changed!\n\nDo you like to save the file?', icon='warning')
            if (answer is None):
               return
            elif (answer):
                self.fileSave()
        
        self.text.delete("1.0","end")
        self.filename = ""
        self.text.edit_modified(False)
        
    def fileOpen (self,filename=''):
        if (type(filename) == tk.Event):
            filename=""
        if filename == "":
            filename = filedialog.askopenfilename(
                initialdir=os.path.dirname(self.filename),
                filetypes=self.filetypes)
        if filename != "":
            self.text.delete('1.0','end')
            file = open(filename,"r")
            for line in file:
                self.text.insert('end',line)
            self.filename = filename
            self.message(f"File {filename} was opened!")
            self.ImageUpdate()
            self.setAppTitle("PumlEditor 2022 - " + os.path.basename(self.filename))
            self.text.updateHighLights()
            self.text.edit_modified(False)
    def fileSave (self,evt=None):
        if self.filename == "":
            self.fileSaveAs
        else:
            fin = open(self.filename, "w")
            fin.write(self.text.get("1.0","end"))
            fin.close()
            self.ImageUpdate()            
            self.setAppTitle("PumlEditor 2022 - " + os.path.basename(self.filename))
            self.text.edit_modified(False)
    def fileSaveAs (self):        
        filename=filedialog.asksaveasfilename(
            title='Select filename to save',
            filetypes=self.filetypes,
            initialdir=os.path.dirname(self.filename))
        if filename != "":
            self.filename = filename
            self.fileSave()
    def fileInsert (self):
        if self.insertfile == "" and self.filename == "":
            initialdir = os.getcwd()
        elif self.insertfile == "":
            initialdir = os.path.dirname(self.filename)
        else:
            initialdir = os.path.dirname(self.insertfile)
        
        file = filedialog.askopenfilename(filetypes=self.filetypes,
            initialdir=initialdir)
        if file:
            self.insertfile = file
            with open(file, "r+") as f:
                self.text.insert(tk.INSERT, f.read())
            
    def text2url (self):
        txt=self.text.get('1.0','end')
        dia = self.getDiaType()
        url=self.kroki.text2kroki(txt,dia=dia,ext="png")
        self.text.insert('end',"\n"+url)
    def url2text (self):
        url=self.text.get('1.0','end')
        url=re.sub("^\s+","",url)
        if not(bool(re.search("^https://kroki.io.+",url))):
            self.message("Error: Text in Editor seems not to be a kroki URL")
            bg=self.text.cget("background")
            self.text.configure(background="salmon")
            self.root.update_idletasks()
            self.root.after(2000)
            self.text.configure(background=bg)            
        else:
            txt=self.kroki.kroki2dia(url)
            self.text.insert("end","\n"+txt)
    def getDiaType (self):
        if bool(re.search("\\.pml$",self.filename)):
            dia="plantuml"
        elif bool(re.search("\\.dot$",self.filename)):
            dia="graphviz"
        elif bool(re.search("\\.erd$",self.filename)):
            dia="erd"            
        elif bool(re.search("\\.dit$",self.filename)):
            dia="ditaa"
        else:
            dia="ditaa"
        return(dia)
    def ImageUpdate (self):
        imgfile = re.sub(".[a-z]{3,4}$",".png",self.filename)
        dia = self.getDiaType()
        try: 
            self.kroki.dia2file(self.filename,dia=dia,imagefile=imgfile)
            if os.path.exists(imgfile):
                self.image.configure(file=imgfile)
                self.message(f"Displaying {imgfile}")
                self.root.title("PumlEditor 2022 - " + os.path.basename(self.filename))
            else:
                self.message("Image file was not downloaded!")
        except:
            bg=self.text.cget("bg")
            self.text.configure(bg='salmon')
            self.root.update_idletasks()
            self.root.after(2000)
            self.text.configure(bg=bg)
            self.message("Error in diagram code!")
    def templateClass (self):
        self.text.delete('1.0', 'end')
        self.text.insert("end",'''@startuml
' https://plantuml.com/class-diagram
left to right direction
skinparam roundcorner 10
skinparam linetype ortho
skinparam shadowing false
skinparam handwritten false
!theme vibrant
skinparam class {
    BackgroundColor #eeeeee
    ArrowColor #2688d4
    ArrowThickness 1
    BorderColor #2688d4
    BorderThickness 1
}
class BaseClass {
    - self.privar
    # self.protvar
    + self.pubvar
    + self.pubMethod()
    # self.ProtMethod()
    - self.PrivMethod()
}
class ChildClass {
    - self.privar
    + self.pubMethod()
}

class Component {
    - self.priv
    + self.pubMethod()
}
Component --* BaseClass
ChildClass --> BaseClass
@enduml
''')

    def templateLists (self,typecmd="listfonts",comment="https://plantuml.com/font"):
        self.text.delete('1.0', 'end')
        self.text.insert("end",f"""@startuml
{typecmd}
' URL: {comment}
@enduml
""")
        self.text.updateHighLights()

    def templateDitaa (self):
        self.text.delete('1.0', 'end')
        self.text.insert("end",'''@startuml
' https://plantuml.com/ditaa
ditaa

+--------+   /-------\    +-------+
| cPNK   +---+ ditaa +--> |       |
|  Text  |   +-------+    |diagram|
|Document|   |!magic!|    | cEFF  |
|     {d}|   |       |    |       |
+---+----+   \-------/    +-------+
    :                         ^
    |       Lots of work      |
    \-------------------------/
@enduml
'''
)
        self.text.updateHighLights()

    def templateLaTeX (self):
        self.text.delete('1.0', 'end')
        self.text.insert("end",'''@startuml
' https://plantuml.com/ascii-math
:<latex>\int_0^1f(x)dx</latex>;
@enduml
'''
)
        self.text.updateHighLights()

    def templateMindmap (self):
        self.text.delete('1.0', 'end')
        self.text.insert("end",'''@startmindmap
' https://plantuml.com/mindmap-diagram
<style> 
mindmapDiagram {  
   node    {  
        BackgroundColor skyblue  
   }  
   .salmon {  
        BackgroundColor salmon
   } 
} 
</style> 
* A 
** A1 
** A2 
* B 
- C 
-- C1 <<salmon>> 
-- C2 
@endmindmap''')
        self.text.updateHighLights()

    def templateDatabase (self):
        db_uml = '''@startuml
!define primary_key(x) <b><color:#b8861b><&key></color> x</b>
!define foreign_key(x) <color:#aaaaaa><&key></color> x
!define column(x) <color:#efefef><&media-record></color> x
' make the table bold '
!define table(x) entity "**x**" as x << (T, #56b8ff) >>

left to right direction
skinparam roundcorner 10
skinparam linetype ortho
skinparam shadowing false
skinparam handwritten false
!theme vibrant
skinparam class {
    BackgroundColor #eeeeee
    ArrowColor #2688d4
    ArrowThickness 2
    BorderColor #2688d4
    BorderThickness 2
}
table( user ) {
  primary_key( id ): UUID 
  column( isActive ): BOOLEAN 
  foreign_key( cityId ): INTEGER <<FK>>
}
table( city ) {
  primary_key( id ): UUID 
  column( name ): TEXT
  column( country ): TEXT
  column( postCode ): INTEGER
}
user }|--|| city
@enduml
'''
        self.text.delete('1.0', 'end')
        self.text.insert('end', db_uml)
    def _Exit(self):
        if (self.text.edit_modified()):
            answer = mbox.askyesnocancel('Question ...', 'Text was changed!\n\nDo you like to save the file\nbefore you quit the application?', icon='warning')
            if (answer is None):
               return
            elif (answer):
                self.fileSave()
            sys.exit(0)
        else:
            super()._Exit()
        
        
    def _About (self):
        mbox.showinfo(title="About PumlEditor",message="PumlEditor 2022\nAuthor: Detlef Groth\nUniversity of Potsdam")

def main(argv):
    root=tk.Tk()
    root.geometry("300x200")
    pedit = PumlEditor(root)
    root.title("PumlEditor 2022")
    if len(argv) > 1:
        if os.path.exists(sys.argv[1]):
            pedit.fileOpen(sys.argv[1])
    pedit.mainLoop() 
            
if __name__ == '__main__':
    main(sys.argv)