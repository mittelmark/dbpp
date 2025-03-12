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

VERSION="0.4.0"    # 2025

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
       if re.search(r"^#'\s+title:",line):
          line=re.sub(r"^#'\s+title:\s+(.+)","#### \\1",line)
          out.write(line+"\n")          
       elif re.search(r"^#'\s+author:",line):
          line=re.sub(r"^#'\s+author:\s+(.+)","##### \\1",line)
          out.write(line+"\n")          
       elif re.search(r"^#'\s+date:",line):
          line=re.sub(r"^#'\s+date:\s+(.+)","##### \\1",line)
          out.write(line+"\n")
       elif re.search(r"^\s*#' ",line):
          line=re.sub(r"^\s*?#' (.*)\n","\\1",line)
          out.write(line+"\n")
       elif re.search(r"^\s*#'\s*\n",line):          
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
       if ilist and re.search(r"^\s{1,3}-",line):
          line=">"+line[1:]
       elif ilist and re.search(r"^\s*$",line):          
          ilist=False
       if not(ifenc) and re.search(r"^>\s{1,2}```",line):
          ifenc=True
       elif ifenc and re.search(r"^>{0,1}\s{1,3}```",line):
          line="> ```\n"
          ifenc = False
       elif ifenc:          
          line=">"+line
       out.write(line)
    file.close()
    out.close()

def main (argv):
    global head
    global VERSION
    cssfile=""
    if len(argv)== 4:
        if not(argv[3].endswith(".css")):
            print("Error: Last filename must be a CSS file and have extension .css")
            exit()
        elif not(os.path.exists(argv[3])):
            print(f"Error: Last stylesheet file '{argv[3]}' does not exists!")
            exit()
            
        else:
            cssfile=argv[3]
            argv=argv[0:-1]
    if len(argv)== 3:
        if not(argv[1].endswith(".md")) and argv[2].endswith('.md'):
            extract(argv[1],argv[2]) 
        elif argv[1].endswith(".md") and   argv[2].endswith(".md"):
            print("conversion of two markdown files")
            md2gitlabmd(argv[1], argv[2]) 
        elif argv[2].endswith('.html'):
            if not(mkd):
                print("Markdown library missing!\nYou must install the Python3 libraries\n Markdown and the extensions like so:\n")
                print("pip3 install pymdown-extensions --user\n")
            else:
                if not(argv[1].endswith(".md")):
                    extract(argv[1],'temp.md')
                    mdfile="temp.md"
                else:
                    mdfile=argv[1]
                with open(mdfile, "r", encoding="utf-8") as input_file:
                    text = input_file.read()
                html = md.convert(text)
                head=re.sub("__TITLE__",os.path.basename(argv[1]),head)
                if (cssfile != ""):
                    head=re.sub("__STYLE__",f"<link rel=\"stylesheet\" href=\"{cssfile}\">",head)
                elif  (os.path.exists("style.css")):
                    head=re.sub("__STYLE__","<link rel=\"stylesheet\" href=\"style.css\">",head)
                else:
                    head=re.sub("__STYLE__","",head)
                with open(argv[2], "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
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
        print("\nCopyright: @ Detlef Groth, University of Potsdam, 2019-2025")
        print("License:   MIT\n")
    
if __name__ == '__main__':        
    main(sys.argv)        

