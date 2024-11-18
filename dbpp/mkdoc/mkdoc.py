#!/usr/bin/python3
import sys
import re
import os
try:
    import markdown
    md = markdown.Markdown(extensions=['pymdownx.superfences'])
    mkd=True
except:
    mkd = False

head="""    
<HTML>
    <HEAD>
        <TITLE>
        Documentation __TITLE__
        </TITLE>
<style>
/* minimal style for documentation */
* {  box-sizing: border-box; }

body {
  color: #333;
  margin: 0 auto;
  max-width: 50em;
  font-family:  "Alegreya", "Georgia", "Garamond", serif;
  line-height: 1.5;
  padding: 2em 1em;
}

h1 {   font-size: 2.5em ; text-align: center; }
h2 {   font-size: 2.0em;  }
h3 {   font-size: 1.5em }
h4 {   font-size: 1.4em; }
h5 {   font-size: 1.2em; }
h2, h3 {  margin-top: 1.5em; }
h4, h5  { text-align:center; margin: 0.3em 0em; }

code {   
    font-size: 90%; 
    font-family:  "Lucida Console", "Courier", monospace;
}
pre {
    font-family:  "Monaco", monospace;
    border-top: 0.1em #9ac solid;
    background: #e9f6ff;
    padding: 10px;
    border-bottom: 0.1em #9ac solid;
}

a:link {  color: #34c; text-decoration: none; }

ul {
  list-style-type: square;
}
</style>
<!-- Custom Style -->
__STYLE__
</HEAD>
<BODY>

<h1>Documentation __TITLE__</h1>
"""
foot="""
</BODY>
</HTML>
"""
def extract (infile,outfile):
    file = open(infile, 'r');
    out  = open(outfile, 'w');
    for line in file:
       if re.search("^#'\s+title:",line):
          line=re.sub("^#'\s+title:\s+(.+)","#### \\1",line)
          out.write(line+"\n")          
       elif re.search("^#'\s+author:",line):
          line=re.sub("^#'\s+author:\s+(.+)","##### \\1",line)
          out.write(line+"\n")          
       elif re.search("^#'\s+date:",line):
          line=re.sub("^#'\s+date:\s+(.+)","##### \\1",line)
          out.write(line+"\n")
       elif re.search("^\s*#' ",line):
          line=re.sub("^\s*?#' (.*)\n","\\1",line)
          out.write(line+"\n")
       elif re.search("^\s*#'\s*\n",line):          
          out.write("\n")
    file.close()
    out.close()
def md2gitlabmd (infile,outfile):
    # do a conversion to gitlab markdown
    file = open(infile, 'r');
    out  = open(outfile, 'w');
    ilist=False
    ifenc=False
    for line in file:
       if re.search("^> - ",line):
          ilist=True
       if ilist and re.search("^\s{1,3}-",line):
          line=">"+line[1:]
       elif ilist and re.search("^\s*$",line):          
          ilist=False
       if not(ifenc) and re.search("^>\s{1,2}```",line):
          ifenc=True
       elif ifenc and re.search("^>{0,1}\s{1,3}```",line):
          line="> ```\n"
          ifenc = False
       elif ifenc:          
          line=">"+line
       out.write(line)
    file.close()
    out.close()
    
if __name__ == '__main__':        
    cssfile=""
    if len(sys.argv)== 4:
        if not(sys.argv[3].endswith(".css")):
            print("Error: Last filename must be a CSS file and have extension .css")
            exit()
        elif not(os.path.exists(sys.argv[3])):
            print(f"Error: Last stylesheet file '{sys.argv[3]}' does not exists!")
            exit()
            
        else:
            cssfile=sys.argv[3]
            sys.argv=sys.argv[0:-1]
    if len(sys.argv)== 3:
        if not(sys.argv[1].endswith(".md")) and sys.argv[2].endswith('.md'):
            extract(sys.argv[1],sys.argv[2]) 
        elif sys.argv[1].endswith(".md") and   sys.argv[2].endswith(".md"):
            print("conversion of two markdown files")
            md2gitlabmd(sys.argv[1], sys.argv[2]) 
        elif sys.argv[2].endswith('.html'):
            if not(mkd):
                print("Markdown library missing!\nYou must install the Python3 libraries\n Markdown and the extensions like so:\n")
                print("pip3 install pymdown-extensions --user\n")
            else:
                if not(sys.argv[1].endswith(".md")):
                    extract(sys.argv[1],'temp.md')
                    mdfile="temp.md"
                else:
                    mdfile=sys.argv[1]
                with open(mdfile, "r", encoding="utf-8") as input_file:
                    text = input_file.read()
                html = md.convert(text)
                head=re.sub("__TITLE__",os.path.basename(sys.argv[1]),head)
                if (cssfile != ""):
                    head=re.sub("__STYLE__",f"<link rel=\"stylesheet\" href=\"{cssfile}\">",head)
                elif  (os.path.exists("style.css")):
                    head=re.sub("__STYLE__","<link rel=\"stylesheet\" href=\"style.css\">",head)
                else:
                    head=re.sub("__STYLE__","",head)
                with open(sys.argv[2], "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
                    output_file.write(head+html+foot)
    else:
        print("mkdoc.py %s - Markdown documentation tool\n\nExtract or convert Markdown code after a `#'` character sequence.\n" % VERSION)
        print("Usage: mkdoc.py infile outfile [cssfile]")
        print("       infile: source code file")
        print("       outfile: Markdown (.md) or HTML (.html) output file")
        print("\nThe Markdown outfile can be processed to html for instance using the syntax:")
        print("       pandoc -i outfile.md -o outfile.html -s --css pandoc.css")
        print("\nAlternatively you can convert directly to HTML like so:")
        print("       mkdoc.py infile.md outfile.html")
        print("\nTo enable direct HTML conversion you need to install the Python package\npymdown-extensions like so:")
        print("       pip3 install pymdown-extensions --user")
        print("\nTo change the look and feel of the output HTML file,\nyou can place a file style.css in the current directory!")
        print("\nCopyright: @ Detlef Groth, University of Potsdam, 2019-2021")
        print("License:   MIT\n")
        

